#!/usr/bin/env python3

def format_wordmap_kotus_sanalista(wordmap):
    kotus_xml = '    <st><s>' + wordmap['lemma'] + '</s>'
    if wordmap['homonym'] != '0':
        kotus_xml += '<hn>' + wordmap['homonym'] + '<hn>'
    kotus_xml += '<t>'
    if wordmap['kotus_tn'] != '0':
        kotus_xml += '<tn>' + wordmap['kotus_tn'] + '</tn>'
    else:
        kotus_xml += '<tn>99</tn>'
    if wordmap['kotus_av'] and wordmap['kotus_av'] != 'False':
        kotus_xml += '<av>' + wordmap['kotus_av'] + '</av>'
    kotus_xml += '</t></st>'
    return kotus_xml


