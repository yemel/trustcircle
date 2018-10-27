from __future__ import unicode_literals

import re
import calendar

from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from randomslugfield import RandomSlugField


class Circle(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Circle, self).save(*args, **kwargs)
        Membership.objects.get_or_create(circle=self, user=self.owner)

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User)
    circle = models.ForeignKey(Circle)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'circle')

    def __unicode__(self):
        return u'%s at %s' % (self.user.email, self.circle.name)


class Issue(models.Model):
    circle = models.ForeignKey(Circle)

    request_date = models.DateTimeField()
    request_html = models.CharField(max_length=100000, null=True, blank=True)
    request_text = models.CharField(max_length=100000, null=True, blank=True)

    digest_date = models.DateTimeField()
    digest_html = models.CharField(max_length=100000, null=True, blank=True)
    digest_text = models.CharField(max_length=100000, null=True, blank=True)

    slug = RandomSlugField(length=10, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(null=True)

    def status(self):
        now = datetime.now()
        if now < self.request_date:
            return 'PENDING'
        elif self.request_date < now < self.digest_date:
            return 'REQUESTING'
        elif not self.published:
            return 'READY'
        else:
            return 'PUBLISHED'

    def request_inbox(self):
        return self._inbox_email('call')

    def update_inbox(self):
        return self._inbox_email('update')

    def digest_inbox(self):
        return self._inbox_email('digest')

    def _inbox_email(self, kind):
        return '%s <%s+%s@go.trustcircle.xyz>' % (self.circle.name, kind, self.slug)

    def noreply_email(self):
        return '%s <noreply@go.trustcircle.xyz>' % self.circle.name

    def get_request_html(self):
        m = re.match('.*<body>(.*)</body>.*', self.request_html or '')
        return m and m.group(1) or self.request_html

    def get_digest_html(self):
        m = re.match('.*<body>(.*)</body>.*', self.digest_html or '')
        return m and m.group(1) or self.digest_html

    @staticmethod
    def find(sender, recipient):
        match = re.match('(call|digest)\+(.*)@go\.trustcircle\.xyz', recipient)
        slug = match and match.group(2) or None
        return Issue.objects.filter(circle__owner__email=sender, slug=slug).last()

    @staticmethod
    def create(cirlce):
        last_issue = cirlce.issue_set.last()

        if last_issue:
            now = last_issue.digest_date + timedelta(day=1)
        else:
            now = datetime.now()

        last_day = calendar.monthrange(now.year, now.month)[1]

        digest = datetime(now.year, now.month, last_day)
        request = digest - timedelta(days=5)

        return Issue.objects.create(circle=cirlce, request_date=request, digest_date=digest)

    def __unicode__(self):
        return u'%s | %s %s' % (self.circle.name, calendar.month_name[self.digest_date.month], self.digest_date.year)


class Message(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Issue)
    data_html = models.CharField(max_length=100000, null=True, blank=True)
    data_text = models.CharField(max_length=100000, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'issue')

    @staticmethod
    def find(sender, recipient):
        match = re.match('update\+(.*)@go\.trustcircle\.xyz', recipient)
        slug = match and match.group(1) or None
        return Message.objects.filter(user__email=sender, issue__slug=slug).last()

    def get_html(self):
        m = re.match('.*<body>(.*)</body>.*', self.data_html or '')
        return m and m.group(1)

    def __unicode__(self):
        return u'%s at %s' % (self.user.email, self.issue)
