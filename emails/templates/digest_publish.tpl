{% extends "mail_templated/base.tpl" %}

{% block subject %}
{{ issue }}
{% endblock %}

{% block body %}
{{ issue.digest_text }}
{% endblock %}

{% block html %}
{{ issue.get_digest_html|safe }}
{% endblock %}
