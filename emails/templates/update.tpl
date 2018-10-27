{% extends "mail_templated/base.tpl" %}

{% block subject %}
Call for updates: {{ issue }}
{% endblock %}

{% block body %}
{{ issue.request_text }}
{% endblock %}

{% block html %}
{{ issue.get_request_html|safe }}
{% endblock %}
