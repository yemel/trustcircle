{% extends "mail_templated/base.tpl" %}

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
    <b>{{ message.user.get_full_name }}</b><br/><br/>

    {{ message.get_html|safe }}
    <br/><br/><br/>
    {% endfor %}
{% endblock %}
