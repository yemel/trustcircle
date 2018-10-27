{% extends "mail_templated/base.tpl" %}

{% block subject %}
[Check] Digest: {{ issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this digest:
-----

{{ issue.digest_text }}
{% endblock %}

{% block html %}
Got it, I'm going to send this digest:<br/>
-----<br/><br/>

{{ issue.get_digest_html|safe }}
{% endblock %}
