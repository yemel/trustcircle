{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
Call for updates: {{ message.issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this update:
-----

{{ message.data_text }}
{% endblock %}

{% block html %}
I'm going to send this update:<br/>
<hr style="margin-bottom:1rem;"/>

{{ message.data_text|apply_markup:"markdown" }}
{% endblock %}
