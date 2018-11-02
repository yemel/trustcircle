{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
{{ issue }}
{% endblock %}

{% block body %}
{{ issue.digest_text }}
{% endblock %}

{% block html %}
{{ issue.digest_html|safe }}
{% endblock %}
