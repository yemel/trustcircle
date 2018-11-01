{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
[Check] Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this call for updates:
-----

{{ issue.request_text }}
{% endblock %}

{% block html %}
Got it, I'm going to send this call for updates:<br/>
<hr style="margin-bottom:1rem;"/>

{{ issue.request_text|apply_markup:"markdown" }}
{% endblock %}
