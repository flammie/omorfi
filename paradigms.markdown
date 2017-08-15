---
layout: page
title: Paradigms
---
# Paradigms

_This is an automatically generated documentation based on omorfilexical database._

Paradigms are sub-groups of lexemes that have unique morpho-phonological features. In omorfi database there is a unique paradigm for every possible combination of certain features:

* Universal Part-of-speech
* Morphophonology, such as: vowel harmony, gradation pattern,  stem variations and allomorph selection
* Other morphotactic limitations, such as: only plurals allowed,  obligatory possessive suffixes, etc.

<table id="paradigmtable" class="display">
<thead>
<tr>
<th>Paradigm</th>
</tr>
</thead>
<tbody>
{% for page in site.pages %}
{% if page.paradigm %}
<tr><td><a href="paradigms/{{page.paradigm}}.html">{{page.paradigm}}</a></td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>


<!-- vim: set ft=markdown:-->
