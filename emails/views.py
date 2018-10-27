
from models.models import Message, Issue
from mail_templated import EmailMessage

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def get_message_id(headers):
    import json
    headers = json.loads(headers)
    header = filter(lambda x: x[0] == 'Message-Id', headers)
    return header and header[0][1] or ''


@csrf_exempt
def inbox(request):
    """ This method handles incoming emails. We expect 3 types of emails:
        * The circle owner patches the request text for the next issue.
        * A member patches its message for this issue.
        * The circle owner patches the digest to be sent to the circle.

        A response is sent to confirm the patch or inform about errors.
    """
    sender = request.POST.get('sender')
    recipient = request.POST.get('recipient')

    stripped_html = request.POST.get('stripped-html')
    stripped_text = request.POST.get('stripped-text')
    message_id = get_message_id(request.POST.get('message-headers'))

    print 'News Message'
    print request.POST.get('stripped-html')
    print request.POST.get('message-headers')

    issue = Issue.find(sender, recipient)
    message = Message.find(sender, recipient)

    if issue and recipient in issue.request_inbox():
        # TODO: Validate State.

        issue.request_html = stripped_html
        issue.request_text = stripped_text
        issue.save()

        send_email('request_ok.tpl', {'issue': issue}, issue.request_inbox(), sender, thread=message_id)

    elif issue and recipient in issue.digest_inbox():
        # TODO: Validate State.

        issue.digest_html = stripped_html
        issue.digest_text = stripped_text
        issue.save()

        send_email('digest_ok.tpl', {'issue': issue}, issue.digest_inbox(), sender, thread=message_id)

    elif message:
        # TODO: Validate State.

        message.data_html = stripped_html
        message.data_text = stripped_text
        message.save()

        send_email('update_ok.tpl', {'message': message}, message.issue.update_inbox(), sender, thread=message_id)

    return HttpResponse('Thanks')


def send_email(template, context, from_email, to, thread=None):
    to = [to] if isinstance(to, basestring) else to
    headers = thread and {'In-Reply-To': thread} or {}
    msg = EmailMessage(template, context, from_email=from_email, to=to, headers=headers)
    msg.send()
    print 'sending email: %s -> %s' % (from_email, to)


def send_request(issue):
    send_email('request.tpl', {'issue': issue}, issue.request_inbox(), issue.circle.owner.email)


def send_update(issue):
    members = issue.circle.membership_set.all()
    for member in members:
        Message.objects.get_or_create(user=member.user, issue=issue)
        send_email('update.tpl', {'issue': issue}, issue.update_inbox(), member.user.email)


def send_digest_check(issue):
    if not issue.digest_html:  # render base digest
        messages = issue.message_set.filter(data_html__isnull=False).order_by('user__first_name')
        context = {'issue': issue, 'messages': messages}
        msg = EmailMessage('digest_base.tpl', context)
        msg.render()

        issue.digest_text = msg.body
        issue.digest_html = msg.alternatives[0][0]
        issue.save()

    send_email('digest_ok.tpl', {'issue': issue}, issue.digest_inbox(), issue.circle.owner.email)


def send_digest(issue):
    recipients = issue.circle.membership_set.values_list('user__email', flat=True)
    send_email('digest_publish.tpl', {'issue': issue}, issue.noreply_email(), recipients)
