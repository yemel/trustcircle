{% extends "mail_templated/base.tpl" %}

{% block subject %}
Call for updates: {{ message.issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this update:
-----

{{ message.data_html }}
{% endblock %}

{% block html %}
I'm going to send this update:<br/>
<hr style="margin-bottom:1rem;"/>

{{ message.get_html|safe }}
{% endblock %}
