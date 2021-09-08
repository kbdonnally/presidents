---
layout: base
---

# Hello!

{% assign presidents = site.data.presidents %}

{% for prez in presidents %}
# {{ prez.name }}

{% for item in prez.achievements%}
- {{ item }}
{% endfor %}
{% endfor %}