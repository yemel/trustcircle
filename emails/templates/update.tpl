{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
Call for updates: {{ issue }}
{% endblock %}

{% block body %}
{{ issue.request_text }}
{% endblock %}

{% block html %}
{{ issue.request_text|apply_markup:"markdown" }}
{% endblock %}
