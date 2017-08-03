---
layout: page
title: Omor stuff–Internal codes
---
# omor stuff: some internal short-hand codes in omorfi databases

_This is an automatically generated documentation based on omorfilexical database._

Stuff are internal things, but they appear in database a lot, so you will want to know what they are if you are gonna modify database of affixes.

The stuff is typically used by the file format and/or analysis generators to either define analysis tags or decide whether or not to include the affected string into language model. The default renditions for a handful of omorfi tag formats are provided (only ones that have trivially mapped formatting are included.

<table id="stufftable" class="display">
<thead>
<tr>
<th>Stuff</th>
</tr>
</thead>
<tbody>
{% for page in site.pages %}
{% if page.stuff %}
<tr><td><a href="stuffs/{{page.stuff}}.html">{{page.stuff}}</a></td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>


<!-- vim: set ft=markdown:-->
