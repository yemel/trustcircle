{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
{{ issue }}
{% endblock %}

{% block body %}
{% for message in messages %}
{{ message.user.get_full_name }}

{{ message.data_text }}

{% endfor %}
{% endblock %}

{% block html %}
    {% for message in messages %}
    <b>{{ message.user.get_full_name }}</b><br/>{{ message.data_text|apply_markup:"markdown" }}
    <br/><br/>
    {% endfor %}
{% endblock %}
