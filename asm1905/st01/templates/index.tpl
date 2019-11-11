{% extends "base.tpl" %}

{% block content %}

{% for number in numbers%}
{% include "item.tpl" ignore missing%}
{% else %}
{% endfor %}

{% include "add.tpl" ignore missing%}

{% endblock %}
