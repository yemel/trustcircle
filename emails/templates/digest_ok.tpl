{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
[Check] {{ issue }}
{% endblock %}

{% block body %}
I'm going to send this digest:
-----

{{ issue.digest_text }}
{% endblock %}

{% block html %}
I'm going to send this digest:<br/>
<hr style="margin-bottom:1rem;"/>

{{ issue.digest_text|apply_markup:"markdown" }}
{% endblock %}
