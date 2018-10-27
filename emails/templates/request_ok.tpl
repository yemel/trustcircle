{% extends "mail_templated/base.tpl" %}

{% block subject %}
[Check] Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this call for updates:
-----

{{ issue.request_text }}
{% endblock %}

{% block html %}
Got it, I'm going to send this call for updates:
<hr style="margin-bottom:1rem;"/>

{{ issue.get_request_html|safe }}
{% endblock %}
