---
layout: page
title: Lexemes
---
# Lexemes

_This is an automatically generated documentation based on omorfilexical database._

Lexemes are the word-entries of omorfi, currently we have only documented the ones that are commonly problematic, in terms of unexpected ambiguity, exceptional spelling or anything otherwise worth noting. Full dictionary can be found for the time being in wiktionary, or other such services.


<table id="lexemetable" class="display">
<thead>
<tr>
<th>Lexeme</th>
</tr>
</thead>
<tbody>
{% for page in site.pages %}
{% if page.lexeme %}
<tr><td><a href="lexemes/{{page.lexeme}}.html">{{page.lexeme}}</a></td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>


<!-- vim: set ft=markdown:-->
