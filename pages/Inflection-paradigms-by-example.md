---
layout: default
title: "Inflection paradigms by example"
category: stats
date: 2016-02-08 18:23:58
---


# Inflection tables of example words #

In the tables below we give key forms showing all the differences of each class.The key forms are designed so that they will show all the possible stems that word class can have, and they are used in end user applications such as guesser to help the classifier to see if the class is right. In the examples we use following notations:

  * the bars | tell boundaries of stub, stem and suffix, this should make it clear that each class has unique set of stems and suffixes.
    * if the first column has no bars, there is no stem variation and whole word form is the _stem_
    * if latter columns have only one bar, the stem is formed by deleting whole varying part, and the part before the bar is the _stem_ and the part after the bar is the _suffix_
    * if any of the columns have two bars in a word form, the first and second parts comprise the _stem_, the second part shows the _stem variation_, and third part is the _suffix_
  * _emphasis_ calls attention to subtle differences, even ones that official classification has neglected
  * (parentheses) old, obsolete or otherwise rare form (see source code for exact classification),
  * ?question mark prefix for potentially strange forms, and ??double question mark for ones that sound awkward
  * ~~strikethrough~~ for forms that are deemed ungrammatical, though allowed in the most permissive forms of omorfi, such as comparatives for (nouns and) adjectives that won't really compare.

### Noun examples ###

The word form set of examples for nouns is:

  * singular nominative - which is dictionary entry, and strong stem for vowel final words and class 48, weak stem for consonant final words
  * singular genitive - which gives _weak singular stem_ for vowel final words and _strong singular stem_ for others
  * singular partitive - which gives _consonant stem_ for some words, and the variants of _singular partitive allomorphs_ that apply
  * singular illative - which gives us the variants of _singular illative allomorphs_ that applies, and usually reveals the _stem vowel_
  * singular essive - which gives _consonant stem_ for some words (others than singular partitive does, it is needed)
  * plural inessive - which gives us _weak plural stem_ for vowel final words and _strong plural stem_ for others
  * plural genitive - which gives us set of _plural genitive allomorphs_
  * plural partitive - which gives us set of _plural partitive allomorphs_
  * plural illative - which gives us set of _plural illative allomorphs_ potentially revealing lemma, weak singular stem, consonant stem or partitive allomorph, strong singular stem or illative allomorph, weak plural stem, allomorph, allomorph, strong plural stem or allomorph.
  * ~~plural nominative~~ - is not given unlike in nssl, it does not contribute anything singular genitive does not already do

Noun example table:

| **Singular nominative** | **- genitive** | **- partitive** | **- illative** | **- essive** | **Plural inessive** | **- genitive** | **- partitive** | **- illative** |
|:------------------------|:---------------|:----------------|:---------------|:-------------|:--------------------|:---------------|:----------------|:---------------|
| talo | talo|n | talo|a | talo|on | talo|na | talo|issa | talo|jen (~ talo|in) | talo|ja | talo|ihin |
| asu | asu|n | asu|a | asu|un | asu|na | asu|issa | asu|jen | asu|ja (~ asu|in) | asu|ihin |
| kärry | kärry|n | kärry|ä | kärry|yn | kärry|nä | kärry|issä | kärry|jen (~ kärry|in) | kärry|jä | kärry|ihin |
| mömmö | mömmö|n | mömmö|ä | mömmö|ön | mömmö|nä | mömmö|issä | mömmö|jen (~ mömmö|in) | mömmö|jä | mömmö|ihin |
| uk|ko | uk|o|n | uk|ko|a | uk|ko|on | uk|ko|na | uk|o|issa | uk|ko|jen (~ uk|ko|in) | uk|ko|ja | uk|ko|ihin |
| tik|ku | tik|u|n | tik|ku|a | tik|ku|un | tik|ku|na | tik|u|issa | tik|ku|jen (~ tik|ku|in) | tik|ku|ja | tik|ku|ihin |
| myrk|ky | myrk|y|n | myrk|ky|ä | myrk|ky|yn | myrk|ky|nä | myrk|y|issä | myrk|ky|jen (~ myrk|ky|in) | myrk|ky|jä | myrk|ky|ihin |
| yök|kö | yök|ö|n | yök|kö|ä | yök|kö|ön | yök|kö|nä | yök|ö|issä | yök|kö|jen (~ yök|kö|in) | yök|kö|jä | yök|kö|ihin |
| hap|po | hap|o|n | hap|po|a | hap|po|on | hap|po|na | hap|o|issa | hap|po|jen (~ hap|po|in) | hap|po|ja | hap|po|ihin |
| lip|pu | lip|u|n | lip|pu|a | lip|pu|un | lip|pu|na | lip|u|issa | lip|pu|jen (~ lip|pu|in) | lip|pu|ja | lip|pu|ihin |
| ryyp|py | ryyp|y|n | ryyp|py|ä | ryyp|py|yn | ryyp|py|nä | ryyp|y|issä | ryp|py|jen (~ ryyp|py|in) | ryyp|py|jä | ryyp|py|ihin |
| törp|pö | törp|ö|n | törp|pö|ä | törp|pö|ön | törp|pö|nä | törp|ö|issä | törp|pö|jen (~ törp|pö|in) | törp|pö|jä | törp|pö|ihin |
| hirt|to | hirt|o|n | hirt|to|a | hirt|to|on | hirt|to|na | hirt|o|issa | hirt|to|jen (~ hirt|to|in) | hirt|to|ja | hirt|to|ihin |
| tort|tu | tort|u|n | tort|tu|a | tort|tu|un | tort|tu|na | tort|u|issa | tort|tu|jen (~ tort|tu|in) | tort|tu|ja | tort|tu|ihin |
| pyt|ty | pyt|y|n | pyt|ty|ä | pyt|ty|yn | pyt|ty|nä | pyt|y|issä | pyt|ty|jen (~ pyt|ty|in) | pyt|ty|jä | pyt|ty|ihin |
| pönt|tö | pönt|ö|n | pönt|tö|ä | pönt|tö|ön | pönt|tö|nä | pönt|ö|issä | pönt|tö|jen (~ pönt|tö|in) | pönt|tö|jä | pönt|tö|ihin |
| te|ko | te|o|n (~ te|’o|n) | te|ko|a | te|ko|on | te|ko|na | te|o|issa (~ te|’o|issa) | te|ko|jen (~ te|ko|in) | te|ko|ja | te|ko|ihin |
| ma|ku | ma|u|n (~ ma|’u|n) | ma|ku|a | ma|ku|un | ma|ku|na | ma|u|issa (~ ma|’u|issa) | ma|ku|jen (~ ma|ku|in) | ma|ku|ja | ma|ku|ihin |
| nä|ky | nä|y|n (~ nä|’y|n) | nä|ky|ä | nä|ky|yn | nä|ky|nä | nä|y|issä (~ nä|’y|issä) | nä|ky|jen (~ nä|ky|in) | nä|ky|jä | nä|ky|ihin |
| nä|kö | nä|ö|n (~ nä|’ö|n)  | nä|kö|ä | nä|kö|ön | nä|kö|nä | nä|ö|issä (~ nä|’ö|issä) | nä|kö|jen (~ nä|kö|in) | nä|kö|jä | nä|kö|ihin |
| ruo|ko | ruo|’o|n | ruo|ko|a | ruo|ko|on | ruo|ko|na | ruo|’o|issa | ruo|ko|jen (~ ruo|ko|in) | ruo|ko|ja | ruo|ko|ihin |
| liu|ku | liu|’u|n | liu|ku|a | liu|ku|un | liu|ku|na | liu|’u|issa | liu|ku|jen (~ liu|ku|in) | liu|ku|ja | liu|ku|ihin |
| he|po | he|vo|n | he|po|a | he|po|on | he|po|na | he|vo|issa | he|po|jen (~ he|po|in) | he|po|ja | he|po|ihin |
| a|pu | a|vu|n | a|pu|a | a|pu|un | a|pu|na | a|vu|issa | a|pu|jen (~ a|pu|in) | a|pu|ja | a|pu|ihin |
| kä|py | kä|vy|n | kä|py|ä | kä|py|yn | kä|py|nä | kä|vy|issä | kä|py|jen (~ kä|py|in) | kä|py|jä  | kä|py|ihin |
| lö|pö | lö|vö|n | lö|pö|ä | lö|pö|ön | lö|pö|nä | lö|vö|issä | lö|pö|jen (~ lö|pö|in) | lö|pö|jä | lö|pö|ihin |
| ve|to | ve|do|n | ve|to|a | ve|to|on | ve|to|na | ve|do|issa | ve|to|jen (~ ve|to|in) | ve|to|ja | ve|to|ihin |
| kui|tu | kui|du|n | kui|tu|a | kui|tu|un | kui|tu|na | kui|du|issa | kui|tu|jen (~ kui|tu|in) | kui|tu|ja | kui|tu|ihin |
| ve|ty | ve|dy|n | ve|ty|ä | ve|ty|yn | ve|ty|nä | ve|dy|issä | ve|ty|jen (~ ve|ty|in) | ve|ty|jä | ve|ty|ihin |
| hää|tö | hää|dö|n | hää|tö|ä | hää|tö|ön | hää|tö|nä | hää|dö|issä | hää|tö|jen (~ hää|tö|in) | hää|tö|jä | hää|tö|ihin |
| run|ko | run|go|n | run|ko|a | run|ko|on | run|ko|na | run|go|issa | run|ko|jen (~ run|ko|in) | run|ko|ja | run|ko|ihin |
| vin|ku | vin|gu|n | vin|ku|a | vin|ku|un | vin|ku|na | vin|gu|issa | vin|ku|jen (~ vin|ku|in) | vin|ku|ja | vin|ku|ihin |
| sän|ky | sän|gy|n | sän|ky|ä | sän|ky|yn | sän|ky|nä | sän|gy|issä | sän|ky|jen (~ sän|ky|in) | sän|ky|jä | sän|ky|ihin |
| ylän|kö | ylän|gö|n | ylän|kö|ä | ylän|kö|ön | ylän|kö|nä | ylän|gö|issä | ylän|kö|jen (~ ylän|kö|in) | ylän|kö|jä | ylän|kö|ihin |
| sam|po | sam|mo|n | sam|po|a | sam|po|on | sam|po|na | sam|mo|issa | sam|po|jen (~ sam|po|in) | sam|po|ja | sam|po|ihin |
| rum|pu | rum|mu|n | rum|pu|a | rum|pu|un | rum|pu|na | rum|mu|issa | rum|pu|jen (~ rum|pu|in) | rum|pu|ja | rum|pu|ihin |
| läm|pö | läm|mö|n | läm|pö|ä | läm|pö|ön | läm|pö|nä | läm|mö|issä | läm|pö|jen (~ läm|pö|in) | läm|pö|jä | läm|pö|ihin |
| kiel|to | kiel|lo|n | kiel|to|a | kiel|to|on | kiel|to|na | kiel|lo|issa | kiel|to|jen (~ kiel|to|in) | kiel|to|ja | kiel|to|ihin |
| huolitel|tu | huolitel|lu|n | huolitel|tu|a | huolitel|tu|un | huolitel|tu|na | huolitel|lu|issa | huolitel|tu|jen (~ huolitel|tu|in) | huolitel|tu|ja | huolitel|tu|ihin |
| epäil|ty | epäil|ly|n | epäil|ty|ä | epäil|ty|yn | epäil|ty|nä | epäil|ly|issä | epäil|ty|jen (~ epäil|ly|in) | epäil|ty|jä | epäil|ty|ihin |
| sisäl|tö | sisäl|lö|n | sisäl|tö|ä | sisäl|tö|ön | sisäl|tö|nä | sisäl|lö|issä | sisäl|tö|jen (~ sisäl|tö|in) | sisäl|tö|jä | sisäl|tö|ihin |
| tun|to | tun|no|n | tun|to|a | tun|to|on | tun|to|na | tun|no|issa | tun|to|jen (~ tun|to|in) | tun|to|ja | tun|to|ihin |
| lin|tu | lin|nu|n | lin|tu|a | lin|tu|un | lin|tu|na | lin|nu|issa | lin|tu|jen (~ lin|tu|in) | lin|tu|ja | lin|tu|ihin |
| män|ty | män|ny|n | män|ty|ä | män|ty|yn | män|ty|nä | män|ny|issä | män|ty|jen (~ män|ny|in) | män|ty|jä | män|ty|ihin |
| kään|tö | kään|nö|n | kään|tö|ä | kään|tö|ön | kään|tö|nä | kään|nö|issä | kään|tö|jen (~ kään|tö|in) | kään|tö|jä | kään|tö|ihin |
| siir|to | siir|ro|n | siir|to|a | siir|to|on | siir|to|na | siir|ro|issa | siir|to|jen (~ siir|to|in) | siir|to|ja | siir|to|ihin |
| lu|ku | lu|vu|n | lu|ku|a | lu|ku|un | lu|ku|na | lu|vu|issa | lu|ku|jen  (~ lu|ku|in) | lu|ku|ja | lu|ku|ihin |
| ky|ky | ky|vy|n | ky|ky|ä | ky|ky|yn | ky|ky|nä | ky|vy|issä | ky|ky|jen (~ ky|vy|in) | ky|ky|jä | ky|ky|ihin |
| ruipelo | ruipelo|n | ruipelo|a | ruipelo|on | ruipelo|na | ruipelo|issa | ruipelo|jen ~ ruipelo|iden ~ ruipelo|itten (~ ruipelo|in) | ruipelo|ja ~ ruipelo|ita | ruipelo|ihin |
| seikkailu | seikkailu|n | seikkailu|a | seikkailu|un | seikkailu|na | seikkailu|issa | seikkailu|jen ~ seikkailu|iden ~ seikkailu|itten (~ seikkailu|in) | seikkailu|ja ~ seikkailu|ita | seikkailu|ihin |
| vehkeily | vehkeily|n | vehkeily|ä | vehkeily|yn | vehkeily|nä | vehkeily|issä | vehkeily|jen ~ vehkeily|iden ~ vehkeily|itten (~ vehkeily|in) | vehkeily|jä ~ vehkeily|itä | vehkeily|ihin |
| jäätelö | jäätelö|n | jäätelö|ä | jäätelö|ön | jäätelö|nä | jäätelö|issä | jäätelö|jen ~ jäätelö|iden ~ jäätelö|itten (~ jäätelö|in) | jäätelö|jä ~ jäätelö|itä | jäätelö|ihin |
| tuomio | tuomio|n | tuomio|ta (~ tuomio|a) | tuomio|on | tuomio|na | tuomio|issa | tuomio|iden ~ tuomio|itten (~ tuomio|in) | tuomio|ita | tuomio|ihin |
| häiriö | häiriö|ön | häiriö|tä (~ häiriö|ä) | häiriö|ön | häiriö|nä | häiriö|issä | häiriö|iden ~ häiriö|itten (~ häiriö|in) | häiriö|itä | häiriö|ihin |
| zombie | zombie|n | zombie|ta (~ zombie|a) | zombie|en | zombie|na | zombie|issa | zombie|iden ~ zombie|itten (~ zombie|in) | zombie|ita | zombie|ihin |
| lepak|ko | lepak|o|n | lepak|ko|a | lepak|ko|on | lepak|ko|na | lepak|o|issa | lepak|ko|jen ~ lepak|o|iden ~ lepak|o|itten | lepak|ko|ja ~ lepak|o|ita | _lepak|ko|ihin ~ lepak|o|ihin_ |
| yksik|kö | yksik|ö|n | yksik|kö|ä | yksik|kö|ön | yksik|kö|nä | yksik|ö|issä | yksik|kö|jen ~ yksik|ö|iden ~ yksik|ö|itten | yksik|kö|jä ~ yksik|ö|itä | _yksik|kö|ihin ~ yksik|ö|ihin_ |
| ruuv|i | ruuv|i|n | ruuv|i|a | ruuv|i|in | ruuv|i|na | ruuv|e|issa | ruuv|ien (~ ruuv|e|in) | ruuv|e|ja | ruuv|e|ihin |
| tyyl|i | tyyl|i|n | tyyl|i|ä | tyyl|i|in | tyyl|i|nä | tyyl|e|issä | tyyl|ien (~ tyyl|e|in) | tyyl|e|jä | tyyl|e|ihin |
| lok|ki | lok|i|n | lok|ki|a | lok|ki|in | lok|ki|na | lok|e|issa | lok|k|ien (~ lok|ke|in) | lok|ke|ja | lok|ke|ihin |
| häk|ki | häk|i|n | häk|ki|ä | häk|ki|in | häk|ki|nä | häk|e|issä | häk|k|ien (~ häk|ke|in) | häk|ke|jä | häk|ke|ihin |
| kup|pi | kup|i|n | kup|pi|a | kup|pi|in | kup|pi|na | kup|e|issa | kup|p|ien (~ kup|pe|in) | kup|pe|ja | kup|pe|ihin |
| tyyp|pi | tyyp|i|n | tyyp|pi|ä | tyyp|pi|in | tyyp|pi|nä | tyyp|e|issä | tyyp|p|ien (~ tyyp|pe|in) | tyyp|pe|jä | tyyp|pe|ihin |
| kort|ti | kort|i|n | kort|ti|a | kort|ti|in | kort|ti|na | kort|e|issa | kort|t|ien (~ kort|te|in) | kort|te|ja | kort|te|ihin |
| skeit|ti | skeit|i|n | skeit|ti|ä | skeit|ti|in | skeit|ti|nä | skeit|e|issä | skeit|t|ien (~ skeit|te|in) | skeit|te|jä | skeit|te|ihin |
| la|ki | la|i|n (~ la|’i|n) | la|ki|a | la|ki|in | la|ki|na | la|e|issa (~ la|’e|issa) | la|k|ien (~ la|ke|in) | la|ke|ja | la|ke|ihin |
| hu|pi | hu|vi|n | hu|pi|a | hu|pi|in | hu|pi|na | hu|ve|issa | hu|p|ien (~ hu|pe|in) | hu|pe|ja | hu|pe|ihin |
| tau|ti | tau|di|n | tau|ti|a | tau|ti|in | tau|ti|na | tau|de|issa | tau|t|ien (~ tau|te|in) | tau|te|ja | tau|te|ihin |
| nih|ti | nih|di|n | nih|ti|ä | nih|ti|in | nih|ti|nä | nih|de|issä | nih|t|ien (~ nih|te|in) | nih|te|jä | nih|te|ihin |
| van|ki | van|gi|n | van|ki|a | van|ki|in | van|ki|na | van|ge|issa | van|k|ien (~ van|ke|in) | van|ke|ja | van|ke|ihin |
| hämmin|ki | hämmin|gi|n | hämmin|ki|ä | hämmin|ki|in | hämmin|ki|nä | hämmin|ge|issä | hämmin|k|ien (~ hämmin|ke|in) | hämmin|ke|jä | hämmin|ke|ihin |
| pel|ti | pel|li|n | pel|ti|ä | pel|ti|in | pel|ti|nä | pel|le|issä | pel|t|ien (~ pel|te|in) | pel|te|jä | pel|te|ihin |
| soin|ti | soin|ni|n | soin|ti|a | soin|ti|in | soin|ti|na | soin|ne|issa | soin|t|ien (~ soin|te|in) | soin|te|ja | soin|te|ihin |
| vien|ti | vien|ni|n | vien|ti|ä | vien|ti|in | vein|ti|nä | vien|ne|issä | vien|t|ien (~ vien|te|in) | vien|te|jä | vien|te|ihin |
| punk (~ punk|ki) | punk|i|n | punk|i|a | punk|i|in | punk|i|na | punk|e|issa | punk|ien (~ punk|e|in) | punk|e|ja | punk|e|ihin |
| zen (~ zeni) | zen|i|n | zen|i|ä | zen|i|in | zen|i|nä | zen|e|issä | zen|ien (~ zen|e|in) | zen|e|jä | zen|e|ihin |
| nei|ti | nei|di|n | nei|ti|ä | nei|ti|in | nei|ti|nä | nei|de|issä | nei|t|ien | nei|te|jä | nei|te|ihin |
| kanaal|i | kanaal|i|n | kanaal|i|a | kanaal|i|in | kanaal|i|na | kanaal|e|issa | kanaal|ien ~ kanaal|e|iden ~ kanaal|e|itten (~ kanaal|e|in) | kanaal|e|ita ~ kanaa|le|ja | kanaal|e|ihin |
| kehvel|i | kehvel|i|n | kehvel|i|ä | kehvel|i|in | kehvel|i|nä | kehvel|e|issä | kehvel|ien ~ kehvel|e|iden ~ kehvel|e|itten (~ kehvel|e|in) | kehvel|e|itä ~ kanaa|le|jä | kehvel|e|ihin |
| stadion (~ stadion|i)| stadion|i|n | stadion|i|a | stadion|i|in | stadion|i|na | stadion|e|issa | stadion|ien ~ stadion|e|iden ~ stadion|e|itten (~ stadion|e|in) | stadion|e|ja ~ stadion|e|ita | stadion|e|ihin |
| besserwisser (~ besserwisser|i) | besserwisser|i|n | besserwisser|i|ä | besserwisser|i|in | besserwisser|i|nä | besserwisser|e|issä | besserwisser|ien ~ besserwisser|e|iden ~ besserwisser|e|itten (~ besserwisser|e|in) | besserwisser|e|jä ~ besserwisser|e|itä | besserwisser|e|ihin |
| sankar|i (~ sankar) | sankar|i|n | sankar|i|a  | sankar|i|in | sankar|i|na | sankar|e|issa | sankar|ien ~ sankar|e|iden ~ sankar|e|itten ~ _sankar|ten_ (~ sankar|e|in) | sankar|e|ita ~ sankar|e|ja | sankar|e|ihin |
| onn|i | onn|e|n | onn|e|a | onn|e|en | onn|e|na | onn|issa | onn|ien | onn|ia | onn|iin |
| kiv|i | kiv|e|n | kiv|e|ä | kiv|e|en | kiv|e|nä | kiv|issä | kiv|ien | kiv|iä | kiv|iin |
| hap|pi | hap|e|n | hap|pe|a | hap|pe|en | hap|pe|na | hap|issa | hap|p|ien | hap|p|ia | hap|p|iin |
| typ|pi | typ|e|n | typ|pe|ä | typ|pe|en | typ|pe|nä | typ|issä | typ|p|ien | typ|p|iä | typ|p|iin |
| no|ki | no|e|n (~ no|’e|n) | no|ke|a | no|ke|en | no|ke|na | no|issa (~ no|’|issa) | no|k|ien | no|k|ia | no|k|iin |
| kä|ki | kä|e|n (~ kä|’e|n) | kä|ke|ä | kä|ke|en | kä|ke|nä | kä|issä (~ kä|’|issä) | kä|k|ien | kä|k|iä | kä|k|iin |
| kor|pi | kor|ve|n | kor|pe|a | kor|pe|en | kor|pe|na | kor|v|issa | kor|p|ien | kor|p|ia | kor|p|iin |
| kil|pi | kil|ve|n | kil|pe|ä | kil|pe|en | kil|pe|nä | kil|v|issä | kil|p|ien | kil|p|iä | kil|p|iin |
| lah|ti | lah|de|n | lah|te|a | lah|te|en | lah|te|na | lah|d|issa | lah|t|ien | lah|t|ia | lah|t|iin |
| leh|ti | leh|de|n | leh|te|ä | leh|te|en | leh|te|nä | leh|d|issä | leh|t|ien | leh|t|iä | leh|t|iin |
| on|ki | on|ge|n | on|ke|a | on|ke|en | on|ke|na | on|g|issa | on|k|ien | on|k|ia | on|k|iin |
| hen|ki | hen|ge|n | hen|ke|ä | hen|ke|en | hen|ke|nä | hen|g|issä | hen|k|ien | hen|k|iä | hen|k|iin |
| sam|pi | sam|me|n | sam|pe|a | sam|pe|en | sam|pe|na | sam|p|ien | sam|p|ia | sam|p|iin |
| rim|pi | rim|me|n | rim|pe|ä | rim|pe|en | rim|pe|nä | rim|m|issä | rim|p|ien | rim|p|iä | rim|p|iin |
| ar|ki | ar|je|n | ar|ke|a | ar|ke|en | ar|ke|na | ar|j|issa | ar|k|ien | ar|k|ia | ar|k|iin |
| jär|ki | jär|je|n | jär|ke|ä | jär|ke|en | jär|ke|nä | jär|j|issä | jär|k|ien | jär|k|iä | jär|k|iin |
| lah|ti | lah|di|n | lah|ti|a (~ _lah|ta_) | lah|ti|in | lah|ti|na | lah|d|issa | lah|t|ien (~ laht|e|in) | lah|te|ja | lah|t|iin |
| ha|psi | ha|pse|n | ha|pse|a (~ ha|s|ta) | ha|pse|en | ha|pse|na | ha|ps|issa | ha|ps|ien (~ ha|s|ten) | ha|ps|ia | ha|ps|iin |
| su|ksi | su|kse|n | su|kse|a (~ su|s|ta) | su|kse|en | su|kse|na | su|ks|issa | su|ks|ien (~ su|s|ten ~ su|kse|in) | su|ks|ia | su|ks|iin |
| u|ksi | u|ks|en | u|ks|ea ~ u|s|ta | u|kse|en | u|kse|na | u|ks|issa | u|ks|ien ~ u|s|ten | u|ks|ia | u|ks|iin |
| nalle | nalle|n | nalle|a | nalle|en | nalle|na | nalle|issa | nalle|jen (~ nalle|in) | nalle|ja | nalle|ihin |
| nisse | nisse|n | nisse|ä | nisse|en | nisse|nä | nisse|issä | nisse|jen (~nisse|in) | nisse|jä | nisse|ihin |
| nuk|ke | nuk|e|n | nuk|ke|a | nuk|ke|en | nuk|ke|na | nuk|e|issa | nuk|ke|jen (~ nuk|ke|in) | nuk|ke|ja | nuk|ke|ihin |
| jep|pe | jep|e|n | jep|pe|ä | jep|pe|en | jep|pe|nä | jep|e|issä | jep|pe|jen (~ jep|pe|in) | jep|pe|jä | jep|pe|ihin |
| kirj|a | kirj|a|n | kirj|a|a | kirj|a|an | kirj|a|na | kirj|o|issa | kirj|o|jen (~ kirj|a|in) | kirj|o|ja | kirj|o|ihin |
| politiik|ka | politiik|a|n | politiik|ka|a | politiik|ka|an | politiik|ka|na | politiik|o|issa | politiik|ko|jen (~ politiik|ka|in) | politiik|ko|ja | politiik|ko|ihin |
| tip|pa | tip|a|n | tip|pa|a | tip|pa|an | tip|pa|na | tip|o|issa | tip|po|jen (~ tip|pa|in) | tip|po|ja | tip|po|ihin |
| mit|ta | mit|a|n | mit|ta|a | mit|ta|an | mit|ta|na | mit|o|issa | mit|to|jen (~ mit|ta|in) | mit|to|ja | mit|to|ihin |
| vel|ka | vel|a|n | vel|ka|a | vel|ka|an | vel|ka|na | vel|o|issa | vel|ko|jen (~ vel|ka|in) | vel|ko|ja | vel|ko|ihin |
| sal|pa | sal|va|n | sal|pa|a | sal|pa|an | sal|pa|na | sal|vo|issa | sal|po|jen (~ sal|pa|in) | sal|po|ja | sal|po|ihin |
| pa|ta | pa|da|n | pa|ta|a | pa|ta|an | pa|ta|na | pa|do|issa | pa|to|jen (~ pa|ta|in) | pa|to|ja | pa|to|ihin |
| lan|ka | lan|ga|n | lan|ka|a | lan|ka|an | lan|ka|na | lan|go|issa | lan|ko|jen (~ lan|ka|in) | lan|ko|ja | lan|ko|ihin |
| ram|pa | ram|ma|n | ram|pa|a | ram|pa|an | ram|pa|na | ram|mo|issa | ram|po|jen (~ ram|pa|in) | ram|po|ja | ram|po|ihin |
| val|ta | val|la|n | val|ta|a | val|ta|an | val|ta|na | val|lo|issa | val|to|jen (~ val|ta|in) | val|to|ja | val|to|ihin |
| kutsun|ta | kutsun|na|n | kutsun|ta|a | kutsun|ta|an | kutsun|ta|na | kutsun|no|issa | kutsun|to|jen (~ kutsun|ta|in) | kutsun|to|ja | kutsun|to|ihin |
| kysyn|tä | kysyn|nä|n | kysyn|tä|ä | kysyn|tä|än | kysyn|tä|nä | kysyn|nö|issä | kysyn|tö|jen (~ kysyn|tä|in) | kysyn|tö|jä | kysyn|tö|ihin |
| ker|ta | ker|ra|n | ker|ta|a | ker|ta|an | ker|ta|na | ker|ro|issa | ker|to|jen (~ ker|ta|in) | ker|to|ja | ker|to|ihin |
| veran|ta | veran|na|n | veran|ta|a | veran|ta|an | veran|ta|na | veran|no|issa | veran|to|jen | veran|to|ja | veran|to|ihin |
| soittaj|a | soittaj|a|n | soittaj|a|a | soittaj|a|an | soittaj|a|na | soittaj|issa | soittaj|ien (~ soittaj|a|in) | soittaj|ia | soittaj|iin  |
| höpöttäj|ä | höpöttäj|ä|n | höpöttäj|ä|ä | höpöttäj|ä|än | höpöttäj|ä|nä | höpöttäj|issä | höpöttäj|ien (~ höpöttäj|ä|in) | höpöttäj|iä | höpöttäj|iin |
| luok|ka | luok|a|n | luok|ka|a | luok|ka|an | luok|ka|na | luok|issa | luok|k|ien (~ luok|ka|in) | luok|k|ia | luok|k|iin  |
| hölk|kä | hölk|ä|n | hölk|kä|ä | hölk|kä|än | hölk|kä|nä | hölk|issä | hölk|kien (~ hölk|kä|in) | hölk|k|iä | hölk|k|iin |
| kuop|pa | kuop|a|n | kuop|pa|a | kuop|pa|an | kuop|pa|na | kuop|issa | kuop|p|ien (~ kuop|pa|in) | kuop|p|ia | kuop|p|iin  |
| sep|pä | sep|ä|n | sep|pä|ä | sep|pä|än | sep|pä|na | sep|issä | sep|pien (~ sep|pä|in) | sep|p|iä | sep|p|iin |
| rot|ta | rot|a|n | rot|ta|a | rot|ta|an | rot|ta|na | rot|issa | rot|t|ien (~ rot|ta|in) | rot|t|ia | rot|t|iin  |
| kent|tä | kent|ä|n | kent|tä|ä | kent|tä|än | kent|tä|nä | kent|issä | kent|tien (~ kent|tä|in) | kent|t|iä | kent|t|iin |
| sul|ka | sul|a|n | sul|ka|a | sul|ka|an | sul|ka|na | sul|issa | sul|k|ien (~ sul|ka|in) | sul|k|ia | sul|k|iin  |
| näl|kä | näl|ä|n | näl|kä|ä | näl|kä|än | näl|kä|nä | näl|issä | näl|kien (~ näl|kä|in) | näl|k|iä | näl|k|iin |
| vuo|ka | vuo|a|n (~ vuo|’a|n) | vuo|ka|a | vuo|ka|an | vuo|ka|na | vuo|issa (~ vuo|’|issa) | vuo|k|ien (~ vuo|ka|in) | vuo|k|ia | vuo|k|iin  |
| rei|kä | rei|ä|n (~ rei|’ä|n) | rei|kä|ä | rei|kä|än | rei|kä|nä | rei|’|issä | rei|kien (~ rei|kä|in) | rei|k|iä | rei|k|iin |
| lu|pa | lu|va|n | lu|pa|a | lu|pa|an | lu|pa|na | lu|v|issa | lu|p|ien (~ lu|pa|in) | lu|p|ia | lu|p|iin  |
| lei|pä | lei|vä|n | lei|pä|ä | lei|pä|än | lei|pä|nä | lei|v|issä | lei|pien (~ lei|pä|in) | lei|p|iä | lei|p|iin |
| so|ta | so|da|n | so|ta|a | so|ta|an | so|ta|na | so|d|issa | so|t|ien (~ so|ta|in) | so|t|ia | so|t|iin  |
| pöy|tä | pöy|dä|n | pöy|tä|ä | pöy|tä|än | pöy|tä|nä | pöy|d|issä | pöy|tien (~ pöy|tä|in) | pöy|t|iä | pöy|t|iin |
| hon|ka | hon|ga|n | hon|ka|a | hon|ka|an | hon|ka|na | hon|g|issa | hon|k|ien (~ hon|ka|in) | hon|k|ia | hon|k|iin  |
| ken|kä | ken|gä|n | ken|kä|ä | ken|kä|än | ken|kä|nä | ken|g|issä | ken|kien (~ ken|kä|in) | ken|k|iä | ken|k|iin |
| kom|pa | kom|ma|n | kom|pa|a | kom|pa|an | kom|pa|na | kom|m|issa | kom|p|ien (~ kom|pa|in) | kom|p|ia | kom|p|iin  |
| mul|ta | mul|la|n | mul|ta|a | mul|ta|an | mul|ta|na | mul|l|issa | mul|t|ien (~ mul|ta|in) | mul|t|ia | mul|t|iin  |
| syl|tä | syl|lä|n | syl|tä|ä | syl|tä|än | syl|tä|nä | syl|l|issä | syl|tien (~ syl|tä|in) | syl|t|iä | syl|t|iin |
| kun|ta | kun|na|n | kun|ta|a | kun|ta|an | kun|ta|na | kun|n|issa | kun|t|ien (~ kun|ta|in) | kun|t|ia | kun|t|iin  |
| emän|tä | emän|nä|n | emän|tä|ä | emän|tä|än | emän|tä|nä | emän|n|issä | emän|tien (~ emän|tä|in) | emän|t|iä | emän|t|iin |
| sel|kä | sel|jä|n | sel|kä|ä | sel|kä|än | sel|kä|nä | sel|j|issä | sel|kien (~ sel|kä|in) | sel|k|iä | sel|k|iin |
| asem|a | asem|a|n | asem|a|a (~ asem|a|ta) | asem|a|an | asem|a|na | asem|issa | asem|ien (~ asem|a|in) | asem|ia | asem|iin |
| jumal|a ~ jumal | jumal|a|n | jumal|a|a | jumal|a|an | jumal|a|na | jumal|issa | jumal|ien ~ jumal|ten | jumal|ia | jumal|iin |
| po|ika | po|ja|n | po|ika|a | po|ika|an | po|ika|na | po|j|issa | po|ik|ien | po|ik|ia | po|ik|iin |
| probleem|a | probleem|a|n | probleem|a|a | probleem|a|an | probleem|a|na | probleem|issa ~ probleem|o|issa | probleem|o|jen ~ probleem|o|iden ~ probleem|o|itten ~ probleem|ien | probleem|o|ja ~ probleem|o|ita ~ probleem|ia | probleem|iin ~ probleem|o|ihin |
| käpäl|ä | käpäl|ä|n | käpäl|ä|ä | käpäl|ä|än | käpäl|ä|nä | käpäl|issä ~ käpäl|ö|issä | käpäl|ö|jen ~ käpäl|ö|iden ~ käpäl|ö|itten ~ käpäl|ien | käpäl|ö|jä ~ käpäl|ö|itä ~ käpäl|iä | käpäl|iin ~ käpäl|ö|ihin |
| makkar|a | makkar|an | makkar|aa | makkar|aan | makkar|a|na | makkar|o|issa | makkar|oiden | makkar|oita | makkar|oihin |
| häkkyr|ä | häkkyr|än | häkkyr|ää | häkkyr|ään | häkkyr|ä|nä | häkkyr|ö|issä | häkkyr|öiden | häkkyr|öitä | häkkyr|öihin |
| kitar|a | kitar|an | kitar|aa | kitar|aan | kitar|a|na | kitar|o|issa | kitaroiden ~ kitaroitten ~ kitar|ojen | kitaroita ~ kitar|oja | kitar|oihin |
| rakuun|a | rakuun|an | rakuun|aa | rakuun|aan | rakuun|a|na | rakuun|o|issa | rakuun|ojen | rakuun|oja | rakuun|oihin |
| lusik|ka | lusik|an | lusik|kaa | lusik|kaan | lusik|ka|na | lusik|o|issa | lusik|oiden ~ lusik|oitten | lusik|oita | _lusik|koihin ~ lusik|oihin_ |
| kämmek|kä | kämmek|än | kämmek|kää | kämmek|kään | kämmek|kä|nä | kämmek|ö|issä | kämmek|öiden ~ kämmek|öitten | kämmek|öitä | _kämmek|köihin ~ kämmek|öihin_ |
| ulap|pa | ulap|a|n | ulap|pa|a | ulap|pa|an | ulap|pa|na | ulap|o|issa | ulap|o|iden ~ ulap|o|itten | ulap|o|ita | _ulap|po|ihin ~ ulap|o|ihin_ |
| pohat|ta | pohat|a|n | pohat|ta|a | pohat|ta|an | pohat|ta|na | pohat|o|issa | pohat|o|iden ~ pohat|o|itten | pohat|o|ita | _pohat|to|ihin ~ pohat|o|ihin_ |
| soke|a (~ soke|e) | soke|an | soke|a|a (~ soke|e|ta ~ soke|a|ta) | soke|a|an | soke|a|na | soke|issa | soke|iden ~ soke|itten | soke|ita | soke|isiin |
| lipe|ä (~ lipe|e) | lipe|än | lipe|ä|a (~ lipe|e|tä ~ lipe|ä|tä) | lipe|ä|än | lipe|ä|nä | lipe|issä | lipe|iden ~ lipe|itten | lipe|itä | lipe|isiin |
| vanhem|pi | vanhem|ma|n | vanhem|pa|a | vanhem|pa|an | vanhem|pa|na | vanhem|m|issa | vanhem|p|ien | vanhem|p|ia | vanhem|p|iin |
| vaina|a | vaina|a|n | vaina|a|ta | vaina|a|seen | vaina|a|na | vaina|issa | vaina|iden ~ vaina|itten | vaina|ita | vaina|isiin |
| tieno|o | tieno|o|n | tieno|o|ta | tieno|o|seen | tieno|o|na | tieno|issa | tieno|iden ~ tieno|itten | tieno|ita | tieno|isiin |
| leikku|u | leikku|u|n | leikku|u|ta | leikku|u|seen | leikku|u|na | leikku|issa | leikku|iden ~ leikku|itten | leikku|ita | leikku|isiin |
| ma|a | ma|a|n | ma|a|ta | ma|a|han | ma|a|na | ma|issa | ma|iden ~ ma|itten | ma|ita | ma|ihin |
| te|e | te|e|n | te|e|tä | te|e|hen | te|e|nä | te|issä | te|iden ~ te|itten | te|itä | te|ihin |
| ha|i | ha|i|n | ha|i|ta | ha|i|hen | ha|i|na | ha|issa | ha|iden ~ ha|itten | ha|ita | ha|ihin |
| pi|i | pi|i|n | pi|i|tä | pi|i|hin | pi|i|nä | pi|issä | pi|iden ~ pi|itten | pi|itä | pi|ihin |
| ooko|o | ooko|o|n | ooko|o|ta | ooko|o|hon | ooko|o|na | ooko|issa | ooko|iden ~ ooko|itten | ooko|ita | ooko|ihin |
| pu|u | pu|u|n | pu|u|ta | pu|u|hun | pu|u|na | pu|issa | pu|iden ~ pu|itten | pu|ita | pu|ihin |
| py|y | py|y|n | py|y|tä | py|y|hyn | py|y|nä | py|issä | py|iden ~ py|itten | py|itä | py|ihin |
| pä|ä | pä|ä|n | pä|ä|tä | pä|ä|hän | pä|ä|nä | pä|issä | pä|iden ~ pä|itten | pä|itä | pä|ihin |
| kö|ö | kö|ö|n | kö|ö|tä | kö|ö|hön | kö|ö|nä | kö|issä | kö|iden ~ kö|itten | kö|itä | kö|ihin |
| v|uo | v|uon | v|uo|ta | v|uo|hon | v|uo|na | v|oi|ssa | v|o|iden ~ v|o|itten | v|o|ita | v|o|ihin |
| t|ie | t|ie|n | t|ie|tä | t|ie|hen | t|ie|nä | t|ei|ssä | t|e|iden ~ t|e|itten | t|e|itä | t|e|ihin |
| |yö| | |yö|n | |yö|tä | |yö|hön | |yö|nä | |ö|issä | |ö|iden ~ |ö|itten | |ö|itä | |ö|ihin |
| nuga|a | nuga|a|n | nuga|a|ta | nuga|a|han | nuga|a|na | nuga|issa | nuga|iden | nuga|ita | nuga|ihin |
| pate|e | pate|e|n | pate|e|ta | pate|e|hen | pate|e|na | pate|issa | pate|iden | pate|ita | pate|ihin |
| bide|e | bide|e|n | bide|e|tä | bide|e|hen | bide|e|nä | bide|issä | bide|iden | bide|itä | bide|ihin |
| triko|o | triko|o|n | triko|o|ta | triko|o|hon | triko|o|na | triko|issa | triko|iden | triko|ita | triko|ihin |
| ragu|u | ragu|u|n | ragu|u|ta | ragu|u|hun | ragu|u|na | ragu|issa | ragu|iden | ragu|ita | ragu|ihin |
| fondy|y | fondy|y|n | fondy|y|tä | fondy|y|hyn | fondy|y|nä | fondy|issä | fondy|iden | fondy|itä | fondy|ihin |
| miljö|ö | miljö|ö|n | miljö|ö|tä | miljö|ö|hön | miljö|ö|nä | miljö|issä | miljö|iden | miljö|itä | miljö|ihin |
| nougat | nougat|’|n | nougat|’|ta | nougat|’|han | nougat|’|na | nougat|’|issa | nougat|’|iden | nougat|’|ita | nougat|’|ihin |
| parfait | parfait|’|n | parfait|’|ta | parfait|’|hen | parfait|’|na | parafait|’|issa | parfait|’|iden | parfait|’|ita | parfait|’|ihin |
| beignet | beignet|’|n | beignet|’|tä | beignet|’|hen | beignet|’|nä | beignet|’|issä | beignet|’|iden | beignet|’|itä | beignet|’|ihin |
| bordeaux | bordeaux|’|n | bordeaux|’|ta | bordeaux|’|hon | bordeaux|’|na | bordeaux|’|issa | bordeaux|’|iden | bordeaux|’|ita | bordeaux|’|ihin |
| show | show|’|n | show|’|ta | show|’|hun | show|’|na | show|’|issa | show|’|iden | show|’|ita | show|’|ihin |
| monsieur | monsieur|’|n | monsieur|’|tä | monsieur|’|hön | monsieur|’|nä | monsieur|’|issä | monsieur|’|iden | monsieur|’|itä | monsieur|’|ihin |
| tul|i | tul|en | tul|ta | tul|e|en | tul|e|na | tul|issa | tul|ien | tul|ia | tul|iin |
| syl|i | syl|en | syl|tä | syl|e|en | syl|e|nä | syl|i|ssä | syl|ien | syl|iä | syl|iin |
| jouhi | jouh|en | jouh|ta | jouh|e|en | jouh|e|na | jouh|issa | jouh|ien (~ jouh|ten) | jouh|ia | jouh|iin |
| riihi | riih|en | riih|tä | riih|e|en | riih|e|nä | riih|issä | riih|ien (~ riih|ten) | riih|iä | riih|iin |
| ?nei|ti | ?nei|de|n | ?nei|t|tä | ?nei|te|en | ?nei|te|nä ~ ?nei|n|nä | nei|d|issä | nei|t|ien | nei|t|iä | nei|te|ihin |
| ruuh|i | ruuh|en | ruuh|ta | ruuh|e|en | ruuh|e|na | ruuh|issa | ruuh|ien ~ ruuh|ten | ruuh|ia | ruuh|iin |
| hiir|i | hiir|en | hiir|tä | hiir|e|en | hiir|e|nä | hiir|issä | hiir|ien ~ hiir|ten | hiir|iä | hiir|iin |
| mer|i | mer|e|n | _mer|ta_ | mer|e|en | mer|e|nä | mer|issä | mer|ien ~ mer|ten | mer|iä | mer|iin |
| tai|mi | tai|me|n | tai|n|ta ~ tai|me|a | tai|me|en | tai|me|na | taim|issa | tai|m|ien ~ tai|n|ten | tai|m|ia | tai|m|iin |
| lie|mi | lie|me|n | lie|n|tä  ~ lie|me|ä | lie|me|en | lie|me|nä | liem|issä | lie|m|ien ~ lie|n|ten | lie|m|iä | lie|m|iin |
| kaar|i | kaar|en | kaar|ta | kaar|e|en | kaar|e|na | kaar|issa | kaar|ten ~ kaar|ien | kaar|ia | kaar|iin |
| miel|i | miel|en | miel|tä | miel|e|en | miel|e|nä | miel|issä | miel|ten ~ miel|ien | miel|iä | miel|iin |
| kau|si | kau|de|n | kau|t|ta | kau|te|en | kau|te|na | kau|s|issa | kau|s|ien ~ kau|t|ten | kau|s|ia | kau|s|iin |
| köy|si | köy|de|n | köy|t|tä | köy|te|en | köy|te|nä | köy|s|issä | köy|s|ien ~ köy|t|ten | köy|s|iä | köy|s|iin |
| pon|si | pon|ne|n | pon|t|ta | pon|te|en | pon|te|na | pon|s|issa | pon|s|ien | pon|s|ia | pon|s|iin |
| län|si | län|ne|n | län|t|ta | län|te|en | län|te|nä | län|s|issä | län|s|ien | län|s|ia | län|s|iin |
| var|si | var|re|n | var|t|ta | var|te|en | var|te|na | var|s|issa | var|s|ien | var|s|ia | var|s|iin |
| vir|si | vir|re|n | vir|t|tä | vir|te|en | vir|te|nä | vir|s|issä | vir|s|ien | vir|s|iä | vir|s|iin |
| jäl|si | jäl|le|n | jäl|t|tä | jäl|te|en | jäl|te|nä | jäl|s|issä | jäl|s|ien | jäl|s|iä | jäl|s|iin |
| la|psi | la|pse|n |  la|s|ta | la|pse|en | la|pse|na | la|ps|issa | la|ps|ien | la|ps|ia | la|ps|iin |
| vei|tsi | vei|tse|n | vei|s|tä ~ ?vei|tse|ä | vei|tse|en | vei|tse|nä | vei|ts|issä | vei|ts|ien ~ vei|s|ten | vei|ts|iä | vei|ts|iin |
| pei|tsi | pei|tse|n | pei|s|tä ~ _pei|tse|ä_ | pei|tse|en | pei|tse|nä | pei|ts|issä | pei|ts|ien ~ pei|s|ten | pei|ts|iä | pei|ts|iin |
| haa|ksi | haa|hde|n | haa|ht|a | haa|hte|en | haa|hte|na | haa|ks|issa | haa|ks|ien | haa|ks|ia | haa|ks|iin |
| joutsen | joutsen|e|n | joutsen|ta | joutsen|e|en | joutsen|e|na | joutsen|issa | joutsen|ten | joutsen|ia | joutsen|iin |
| siemen | siemen|e|n | siemen|tä | siemen|e|en | siemen|e|nä | siemen|issä | siemen|ten | siemen|iä | siemen|iin |
| ajat|ar | ajat|tare|n | ajat|ar|ta | ajat|tare|en | ajat|tare|na | ajat|tar|issa | ajat|ar|ten | ajat|tar|ia | ajat|ttar|iin |
| tyt|är | tyt|täre|n | tyt|är|tä | tyt|täre|en | tyt|täre|nä | tyt|tär|issä | tyt|är|ten | tyt|tär|iä | tyt|tär|iin |
| i|en | i|kene|n | i|en|tä | i|kene|en | i|kene|nä | i|ken|issä | i|en|ten | i|ken|iä | i|ken|iin |
| ahven | ahven|en | ahven|ta | ahven|e|en | ahven|e|na (~ _ahven|na_) | ahven|issa | ahven|ten | ahven|ia | ahven|iin |
| puheli|n | puheli|me|n | puheli|n|ta | puheli|me|en | puheli|me|na | puheli|m|issa | puheli|n|ten | puheli|m|ia | puheli|m|iin |
| eli|n | eli|me|n | eli|n|tä | eli|me|en | eli|me|nä | eli|m|issä | eli|n|ten | eli|miä | eli|miin |
| heit|in | heit|time|n | heit|in|tä | heit|time|en | heit|time|nä | heit|tim|issä | heit|in|ten | heit|tim|iä | heit|tim|iin |
| pu|in | pu|kime|n | pu|in|ta | pu|kime|en | pu|kime|na | pu|kim|issa | pu|in|ten | pu|kim|ia | pu|kim|iin |
| pyyh|in | pyyh|kime|n | pyyh|in|tä | pyyh|kime|en | pyyh|kime|nä | pyyh|kim|issä | pyyh|in|ten | pyyh|kim|iä | pyyh|kim|iin |
| raa|vin | raa|pime|n | raa|vin|ta | raa|pime|en | raa|pime|na | raa|pim|issa | raa|vin|ten | raa|pim|ia | raa|pim|ivin |
| sär|vin | sär|pime|n | sär|vin|tä | sär|pime|en | sär|pime|nä | sär|pim|issä | sär|vin|ten | sär|pim|iä | sär|pim|iin |
| vaa|din | vaa|time|n | vaa|din|ta | vaa|time|en | vaa|time|na | vaa|tim|issa | vaa|din|ten | vaa|tim|ia | vaa|tim|idin |
| sää|din | sää|time|n | sää|din|tä | sää|time|en | sää|time|nä | sää|tim|issä | sää|din|ten | sää|tim|iä | sää|tim|iin |
| askel|lin | askel|time|n | askel|lin|ta | askel|time|en | askel|time|na | askel|tim|issa | askel|lin|ten | askel|tim|ia | askel|tim|ilin |
| sivel|lin | sivel|time|n | sivel|lin|tä | sivel|time|en | sivel|time|nä | sivel|tim|issä | sivel|lin|ten | sivel|tim|iä | sivel|tim|iin |
| muun|nin | muun|time|n | muun|nin|ta | muun|time|en | muun|time|na | muun|tim|issa | muun|nin|ten | muun|tim|ia | muun|tim|inin |
| kään|nin | kään|time|n | kään|nin|tä | kään|time|en | kään|time|nä | kään|tim|issä | kään|nin|ten | kään|tim|iä | kään|tim|iin |
| kihar|rin | kihar|time|n | kihar|rin|ta | kihar|time|en | kihar|time|na | kihar|tim|issa | kihar|rin|ten | kihar|tim|ia | kihar|tim|irin |
| kier|rin | kier|time|n | kier|rin|tä | kier|time|en | kier|time|nä | kier|tim|issä | kier|rin|ten | kier|tim|iä | kier|tim|iin |
| pol|jin | pol|time|n | pol|jin|ta | pol|kime|en | pol|kime|na | pol|kim|issa | pol|jin|ten | pol|kim|ia | pol|kim|iin |
| sydä|n | sydä|me|n | sydä|n|tä | sydä|me|en | sydä|me|nä (~ _sydä|n|nä_) | sydä|m|issä | sydä|n|ten | sydä|m|iä | sydä|m|iin |
| aakkostami|nen | aakkostami|se|n | aakkostami|s|ta | aakkostami|se|en | aakkostami|se|na | aakkostami|s|issa | aakkostami|s|ten ~ aakkostami|s|ien | aakkostami|s|ia | aakkostami|s|iin |
| kylkiäi|nen | kylkiäi|se|n | kylkiäi|s|tä | kylkiäi|se|en | kylkiäi|se|nä | kylkiäi|s|issä | kylkiäi|s|ten ~ kylkiäi|s|ien | kylkiäi|s|iä | kylkiäi|s|iin |
| vakuutu|s | vakuutu|kse|n | vakuutu|s|ta | vakuutu|kse|en | vakuutu|kse|na | vakuutu|ks|issa | vakuutu|s|ten ~ vakuutu|ks|ien | vakuutu|ks|ia | vakuutu|ks|iin |
| räjäyty|s | räjäyty|kse|n | räjäyty|s|tä | räjäyty|kse|en | räjäyty|kse|nä räjäyty|ks|issä | räjäyty|s|ten ~ räjäyty|ks|ien | räjäyty|ks|iä | räjäyty|ks|iin |
| uro|s | uro|kse|n ~ uro|o|n | uro|s|ta | uro|kse|en ~ uro|o|seen | uro|kse|na ~ uro|o|na | uro|ks|issa ~ uro|issa | uro|s|ten ~ uro|ks|ien ~ uro|iden ~ uro|itten | uro|ks|ia ~ uro|ita | uro|ks|iin ~ uro|isiin |
| aakkosellisuu|s | aakkosellisuu|de|n | aakkosellisuu|t|ta | aakkosellisuu|te|en | aakkosellisuu|te|na | aakkosellisuu|ks|issa | aakkosellisuu|ks|ien | aakkosellisuu|ks|ia | aakkosellisuu|ks|iin |
| köyhyy|s | köyhyy|de|n | köyhyy|t|tä | köyhyy|te|en | köyhyy|te|nä | köyhyy|ks|issä | köyhyy|ks|ien | köyhyy|ks|iä | köyhyy|ks|iin |
| patsa|s | patsa|a|n | patsa|s|ta | patsa|a|seen | patsa|a|na | patsa|issa | patsa|iden | patsa|ita | patsa|isiin |
| asuk|as | asuk|kaa|n | asuk|as|ta | asuk|kaa|seen | asuk|kaa|na | asuk|ka|issa | asuk|ka|iden | asuk|ka|ita | asuk|ka|isiin |
| saap|as | saap|paa|n | saap|as|ta | saap|paa|seen | saap|paa|na | saap|pa|issa | saap|pa|iden | saap|pa|ita | saap|pa|isiin |
| ryp|äs | ryp|pää|n | ryp|äs|tä | ryp|pää|seen | ryp|pää|nä | ryp|pä|issä | ryp|pä|iden | ryp|pä|itä | ryp|pä|isiin |
| rat|as | rat|taa|n | rat|as|ta | rat|taa|seen | rat|taa|na | rat|ta|issa | rat|ta|iden | rat|ta|ita | rat|ta|isiin |
| mät|äs | mät|tää|n | mät|äs|tä | mät|tää|seen | mät|tää|nä | mät|tä|issä | mät|tä|iden | mät|tä|itä | mät|tä|isiin |
| var|as | var|kaa|n | var|as|ta | var|kaa|seen | var|kaa|na | var|ka|issa | var|ka|iden | var|ka|ita | var|ka|isiin |
| i|es | i|kee|n | i|es|tä | i|kee|seen | i|kee|nä | i|ke|issä | i|ke|iden | i|ke|itä | i|ke|isiin |
| ru|is | ru|kii|n | ru|is|ta | ru|kii|seen | ru|kii|na | ru|ki|issa | ru|ki|iden | ru|ki|ita | ru|ka|isiin |
| var|vas | var|paa|n | var|vas|ta | var|paa|seen | var|paa|na | var|pa|issa | var|pa|iden | var|pa|ita | var|pa|isiin |
| sei|väs | sei|pää|n | sei|väs|tä | sei|pää|seen | sei|pää|nä | sei|pä|issä | sei|pä|iden | sei|pä|itä | sei|pä|isiin |
| teh|das | teh|taa|n | teh|das|ta | teh|taa|seen | teh|taa|na | teh|ta|issa | teh|ta|iden | teh|ta|ita | teh|ta|isiin |
| kan|gas | kan|kaa|n | kan|gas|ta | kan|kaa|seen | kan|kaa|na | kan|ka|issa | kan|ka|iden | kan|ka|ita | kan|ka|isiin |
| ham|mas | ham|paa|n | ham|mas|ta | ham|paa|seen | ham|paa|na | ham|pa|issa | ham|pa|iden | ham|pa|ita | ham|pa|isiin |
| al|las | al|taa|n | al|las|ta | al|taa|seen | al|taa|na | al|ta|issa | al|ta|iden | al|ta|ita | al|ta|isiin |
| kin|nas | kin|taa|n | kin|nas|ta | kin|taa|seen | kin|taa|na | kin|ta|issa | kin|ta|iden | kin|ta|ita | kin|ta|isiin |
| ryn|näs | ryn|tää|n | ryn|näs|tä | ryn|tää|seen | ryn|tää|nä | ryn|tä|issä | ryn|tä|iden | ryn|tä|itä | ryn|tä|isiin |
| por|ras | por|taa|n | por|ras|ta | por|taa|seen | por|taa|na | por|ta|issa | por|ta|iden | por|ta|ita | por|ta|isiin |
| kirve|s | kirve|e|n | kirve|s|tä | kirve|e|seen | kirve|e|nä | kirve|issä | kirve|iden | kirve|isiin |
| kauri|s | kauri|i|n | kauri|s|ta | kauri|i|seen | kauri|i|na | kauri|issa | kauri|i|den | kauri|ita | kauri|isiin |
| koira|s | koira|a|n ~ koira|kse|n | koira|s|ta | koira|a|seen ~ koira|kse|en | koira|a|na ~ koira|kse|na | koira|issa ~ koira|ks|issa | koira|iden ~ koira|ks|ien | koira|ita ~ koira|ks|ia | koira|isiin ~ koira|ks|iin |
| mie|s | mie|he|n | mie|s|tä | mie|he|en | mie|he|nä | mie|h|issä | mie|s|ten ~ mie|h|ien | mie|h|iä | mie|h|iin |
| olu|t | olu|e|n | olu|t|ta | olu|e|en | olu|e|na | olu|issa | olu|iden ~ olu|itten | olu|ita | olu|isiin |
| neitsy|t | neitsy|e|n | neitsy|t|tä | neitsy|e|en | neitsy|e|nä | neitsy|issä | neitsy|iden ~ neitsy|itten | neitsy|itä | neitsy|isiin |
| kevä|t | kevä|ä|n | kevä|t|tä | kevä|ä|seen | kevä|ä|nä | kevä|issä | kevä|iden ~ kevä|itten | kevä|itä | kevä|isiin |
| vuosituha|t | vuosituha|nne|n | vuosituha|t|ta | vuosituha|nte|en | vuosituha|nte|na | vuosituha|ns|issa | vuosituha|ns|ien (~ vuosituha|n|ten) | vuosituha|ns|ia | vuosituha|ns|iin |
| aivokuoll|ut | aivokuoll|ee|n | aivokuoll|ut|ta | aivokuoll|ee|seen | aivokuoll|ee|na | aivokuoll|e|issa | aivokuoll|e|iden ~ aivokuoll|e|itten | aivokuoll|e|ita | aivokuoll|e|isiin ~ aivokuoll|e|ihin |
| aste | aste|en | aste|t|ta | aste|e|seen | aste|e|na | aste|issa | aste|iden ~ aste|itten | aste|ita | aste|isiin |
| piste | piste|e|n | piste|t|tä | piste|e|seen | piste|e|nä | piste|issä | piste|iden ~ piste|itten | piste|itä | piste|isiin |
| kastik|e | kastik|kee|n | kastik|et|ta | kastik|kee|seen | kastik|kee|na | kastik|ke|issa | kastik|ke|iden ~ kastik|ke|itten | kastik|ke|ita | kastik|ke|isiin |
| lääk|e | lääk|kee|n | lääk|et|tä | lääk|kee|seen | lääk|kee|nä | lääk|ke|issä | lääk|ke|iden ~ lääk|ke|itten | lääk|ke|itä | lääk|ke|isiin |
| ap|e | ap|pee|n | ap|et|ta | ap|pee|seen | ap|pee|na | ap|pe|issa | ap|pe|iden ~ ap|pe|itten | ap|pe|ita | ap|pe|isiin |
| rip|e | rip|pee|n | rip|et|tä | rip|pee|seen | rip|pee|nä | rip|pe|issä | rip|pe|iden ~ rip|pe|itten | rip|pe|itä | rip|pe|isiin |
| osoit|e | osoit|tee|n | osoit|et|ta | osoit|tee|seen | osoit|tee|na | osoit|te|issa | osoit|te|iden ~ osoit|te|itten | osoit|te|ita | osoit|te|isiin |
| käsit|e | käsit|tee|n | käsit|et|tä | käsit|tee|seen | käsit|tee|nä | käsit|te|issä | käsit|te|iden ~ käsit|te|itten | käsit|te|itä | käsit|te|isiin |
| ko|e | ko|kee|n | ko|et|ta | ko|kee|seen | ko|kee|na | ko|ke|issa | ko|ke|iden ~ ko|ke|itten | ko|ke|ita | ko|ke|isiin |
| pyyh|e | pyyh|kee|n | pyyh|et|tä | pyyh|kee|seen | pyyh|kee|nä | pyyh|ke|issä | pyyh|ke|iden ~ pyyh|ke|itten | pyyh|ke|itä | pyyh|ke|isiin |
| tar|ve | tar|pee|n | tar|vet|ta | tar|pee|seen | tar|pee|na | tar|pe|issa | tar|pe|iden ~ tar|pe|itten | tar|pe|ita | tar|pe|isiin |
| vii|ve | vii|pee|n | vii|vet|tä | vii|pee|seen | vii|pee|nä | vii|pe|issä | vii|pe|iden ~ vii|pe|itten | vii|pe|itä | vii|pe|isiin |
| luo|de | luo|tee|n | luo|det|ta | luo|tee|seen | luo|tee|na | luo|te|issa | luo|te|iden ~ luo|te|itten | luo|te|ita | luo|te|isiin |
| ki|de | ki|tee|n | ki|det|tä | ki|tee|seen | ki|tee|nä | ki|te|issä | ki|te|iden ~ ki|te|itten | ki|te|itä | ki|te|isiin |
| lum|me | lum|pee|n | lum|met|ta | lum|pee|seen | lum|pee|na | lum|pe|issa | lum|pe|iden ~ lum|pe|itten | lum|pe|ita | lum|pe|isiin |
| vuol|le | vuol|tee|n | vuol|let|ta | vuol|tee|seen | vuol|tee|na | vuo|te|issa | vuol|te|iden ~ vuol|te|itten | vuol|te|ita | vuol|te|isiin |
| miel|le | miel|tee|n | miel|let|tä | miel|tee|seen | miel|tee|nä | miel|te|issä | miel|te|iden ~ miel|te|itten | miel|te|itä | miel|te|isiin |
| raken|ne | raken|tee|n | raken|net|ta | raken|tee|seen | raken|tee|na | raken|te|issa | raken|te|iden ~ raken|te|itten | raken|te|ita | raken|te|isiin |
| kiin|ne | kiin|tee|n | kiin|net|tä | kiin|tee|seen | kiin|tee|nä | kiin|te|issä | kiin|te|iden ~ kiin|te|itten | kiin|te|itä | kiin|te|isiin |
| poh|je | poh|kee|n | poh|net|ta | poh|kee|seen | poh|kee|na | poh|ke|issa | poh|ke|iden ~ poh|ke|itten | poh|ke|ita | poh|ke|isiin |
| hyl|je | hyl|kee|n | hyl|net|tä | hyl|kee|seen | hyl|kee|nä | hyl|ke|issä | hyl|ke|iden ~ hyl|ke|itten | hyl|ke|itä | hyl|ke|isiin |
| ori | ori|n (~ ori|hi|n) | ori|t|ta | ori|i|seen (~ ori|hi|sen) | ori|i|na (~ ori|hi|na) | ori|issa | ori|iden ~ ori|itten (~ ori|t|ten ~ ori|h|ien ~ ori|h|itten) | ori|ita (~ ori|h|ia) | ori|isiin ~ ori|ihin (~ ori|h|isin) |
| kiiru | kiiru|n (~ kiiru|hu|n) | kiiru|t|ta | kiiru|u|seen (~ kiiru|hu|sen) | kiiru|u|na (~ kiiru|hu|na) | kiiru|issa | kiiru|iden ~ kiiru|itten (~ kiiru|t|ten ~ kiiru|h|ien ~ kiiru|h|itten) | kiiru|ita (~ kiiru|h|ia) | kiiru|isiin ~ kiiru|ihin (~ kiiru|h|isin) |
| taipale | taipale|e|n | taipale|t|ta | taipale|e|seen | taipale|e|na | taipale|issa | taipale|iden ~ taipale|itten | taipale|ita | taipale|isiin |
| kyynele | kyynele|e|n | kyynele|ttä | kyynele|e|seen | kyynele|e|nä | kyynele|issä | kyynele|iden ~ kyynele|itten | kyynele|itä | kyynele|isiin |
| utare | utare|e|n | utare|t|ta | utare|e|seen | utare|e|na | utare|issa | utare|iden ~ utare|itten | utare|ita | utare|isiin |
| kyynel | kyynel|e|n | kyynel|tä | (kyynel|e|en) | kyynel|e|nä | kyynel|issä | kyynel|ien ~ kyynel|ten | kyynel|iä | kyynel|iin |
| sä|en | sä|kene|n | sä|en|tä | (sä|kene|en) | sä|kene|nä | sä|ken|issä | sä|ken|ien ~ sä|en|ten | sä|ken|iä | sä|ken|iin |
| tai|val | tai|pale|n | tai|val|ta | (tai|pale|en) | tai|pale|na | tai|pal|issa | tai|pal|ien ~ tai|val|ten | tai|pal|ia | tai|pal|iin |
| u|dar | u|tare|n | u|dar|ta | (u|tare|en) | u|tare|na | u|tar|issa | u|tar|ien ~ u|dar|ten | u|tar|ia | u|tar|iin |
| pen|ger | pen|kere|n | pen|ger|tä | (pen|kere|en) | pen|kere|nä | pen|ker|issä | pen|ker|ien ~ pen|ger|ten | pen|ker|iä | pen|ker|iin |
| om|mel | om|pele|n | om|mel|ta | (om|pele|en) | om|pele|na | om|pel|issa | om|pel|ien ~ om|mel|ten | om|pel|ia | om|pel|iin |
| man|ner | man|tere|n | man|ner|ta | (man|tere|en) | man|tere|na | man|ter|issa | man|ter|ien ~ man|ner|ten | man|ter|ia | man|ter|iin |
| kan|nel | kan|tele|n | kan|nel|ta | (kan|tele|en) | kan|tele|na | kan|tel|issa | kan|tel|ien ~ kan|nel|ten | kan|tel|ia | kan|tel|iin |
| kin|ner | kin|tere|n | kin|ner|tä | (kin|tere|en) | kin|tere|nä | kin|ter|issä | kin|ter|ien ~ kin|ner|ten | kin|ter|iä | kin|ter|iin |
| au|er | au|tere|n | au|er|ta | (au|tere|en) | au|tere|na | au|ter|issa | au|ter|ien ~ au|er|ten | au|ter|ia | au|ter|iin |

### Adjective classification set ###

The adjectives are in effect same as nouns, we show two additional forms:

  * comparative - which may have a new _e stem_ not found in nominal cases
  * superlative

The classes of adjectives are a subset of nominal classes, except for the e stems.

| Singular nominative | - genitive | - partitive | - illative | - essive | Plural inessive | - genitive | - partitive | - illative | Comparative | Superlative |
|:--------------------|:-----------|:------------|:-----------|:---------|:----------------|:-----------|:------------|:-----------|:------------|:------------|
| tummahko | tummahko|n | tummahko|a | tummahko|on | tummahko|na | tummahko|jen (~ tummahko|in) | tummahko|ja | tummahko|ihin | tummahko|mpi | tummahko|in |
| valkaistu | valkaistu|n | valkaistu|a | valkaistu|un | valkaistu|na | valkaistu|jen | valkaistu|ja (~ valkaistu|in) | valkaistu|ihin | valkaistu|mpi | valkaistu|in |
| häpäisty | häpäisty|n | häpäisty|ä | häpäisty|yn | häpäisty|t | häpäisty|jä (~ häpäisty|in) | häpäisty|ihin | häpäisty|mpi | häpäisty|in |
| hölö | hölö|n | hölö|ä | hölö|ön | hölö|t | hölö|jen (~ hölö|in) | hölö|jä | hölö|ihin | hölö|mpi | hölö|in |
| kolk|ko | kolk|o|n | kolk|ko|a | kolk|ko|on | kolk|o|t | kolk|ko|jen (~ kolk|ko|in) | kolk|ko|ja | kolk|ko|ihin | kolk|o|mpi | kolk|o|in |
| virk|ku | virk|u|n | virk|ku|a | virk|ku|un | virk|u|t | virk|ku|jen | virk|ku|ja (~ virk|ku|in) | virk|ku|ihin | virk|u|mpi | virk|u|in |
| säik|ky | säik|y|n | säik|ky|ä | säik|ky|yn | säik|y|t | säik|ky|jä (~ säik|ky|in) | säik|ky|ihin | säik|y|mpi | säik|y|in |
| kök|kö | kök|ö|n | kök|kö|ä | kök|kö|ön | kök|ö|t | kök|kö|jen (~ kök|kö|in) | kök|kö|jä | kök|kö|ihin | kök|ö|mpi | kök|ö|in |
| suip|po | suip|o|n | suip|po|a | suip|po|on | suip|o|t | suip|po|jen (~ suip|po|in) | suip|po|ja | suip|po|ihin | suip|o|mpi | suip|o|in |
| ikälop|pu | ikälop|u|n | ikälop|pu|a | ikälop|pu|un | ikälop|u|t | ikälop|pu|jen | ikälop|pu|ja (~ ikälop|pu|in) | ikälop|pu|ihin | ikälop|u|mpi | ikälop|u|in |
| lörp|pö | lörp|ö|n | lörp|pö|ä | lörp|pö|ön | lörp|ö|t | lörp|pö|jen (~ lörp|pö|in) | lörp|pö|jä | lörp|pö|ihin | lörp|ö|mpi | lörp|ö|in |
| velt|to | velt|o|n | velt|to|a | velt|to|on | velt|o|t | velt|to|jen (~ velt|to|in) | velt|to|ja | velt|to|ihin | velt|o|mpi | velt|o|in |
| vimmat|tu | vimmat|u|n | vimmat|tu|a | vimmat|tu|un | vimmat|u|t | vimmat|tu|jen | vimmat|tu|ja (~ vimmat|tu|in) | vimmat|tu|ihin | vimmat|u|mpi | vimmat|u|in |
| ylennet|ty | ylennet|y|n | ylennet|ty|ä | ylennet|ty|yn | ylennet|y|t | ylennet|ty|jä (~ ylennet|ty|in) | ylennet|ty|ihin | ylennet|y|mpi | ylennet|y|in |
| kel|po | kel|vo|n | kel|po|a | kel|po|on | kel|vo|t | kel|po|jen (~ kel|po|in) | kel|po|ja | kel|po|ihin | kel|vo|mpi | kel|vo|in |
| mie|to | mie|do|n | mie|to|a | mie|to|on | mie|do|t | mie|to|jen (~ mie|to|in) | mie|to|ja | mie|to|ihin | mie|do|mpi | mie|do|in |
| viipaloi|tu | viipaloi|du|n | viipaloi|tu|a | viipaloi|tu|un | viipaloi|du|t | viipaloi|tu|jen | viipaloi|tu|ja (~ viipaloi|tu|in) | viipaloi|tu|ihin | viipaloi|du|mpi | viipaloi|du|in |
| yksilöi|ty | yksilöi|dy|n | yksilöi|ty|ä | yksilöi|ty|yn | yksilöi|dy|t | yksilöi|ty|jä (~ yksilöi|ty|in) | yksilöi|ty|ihin | yksilöi|dy|mpi | yksilöi|dy|in |
| len|ko | len|go|n | len|ko|a | len|ko|on | len|go|t | len|ko|jen (~ len|ko|in) | len|ko|ja | len|ko|ihin | len|go|mpi | len|go|in |
| mel|to | mel|lo|n | mel|to|a | mel|to|on | mel|lo|t | mel|to|jen (~ mel|to|in) | mel|to|ja | mel|to|ihin | mel|lo|mpi | mel|lo|in |
| parannel|tu | parannel|lu|n | parannel|tu|a | parannel|tu|un | parannel|lu|t | parannel|tu|jen | parannel|tu|ja (~ parannel|tu|in) | parannel|tu|ihin |
| vähätel|ty | vähätel|ly|n | vähätel|ty|ä | vähätel|ty|yn | vähätel|ly|t | vähätel|ty|jen (~ vähätel|ly|in) | vähätel|ty|jä | vähätel|ty|ihin |
| ven|to | ven|no|n | ven|to|a | ven|to|on | ven|no|t | ven|to|jen (~ ven|to|in) | ven|to|ja | ven|to|ihin |
| mar|to | mar|ro|n | mar|to|a | mar|to|on | mar|ro|t | mar|to|jen (~ mar|to|in) | mar|to|ja | mar|to|ihin |
| kohelo | kohelo|n | kohelo|a | kohelo|on | kohelo|t | kohelo|jen ~ kohelo|iden ~ kohelo|itten (~ kohelo|in) | kohelo|ja ~ kohelo|ita | kohelo|ihin |
| ?epäreilu | epäreilu|n | epäreilu|a | epäreilu|un | epäreilu|t | epäreilu|jen ~ epäreilu|iden ~ epäreilu|itten (~ epäreilu|in) | epäreilu|ja ~ epäreilu|ita | epäreilu|ihin |
| löperö | löperö|n | löperö|ä | löperö|ön | löperö|t | löperö|jen ~ löperö|iden ~ löperö|itten (~ löperö|in) | löperö|jä ~ löperö|itä | löperö|ihin |
| autio | autio|n | autio|ta (~ autio|a) | autio|on | autio|t | autio|iden ~ autio|itten (~ autio|in) | autio|ita | autio|ihin |
| riiviö | riiviö|ön | riiviö|tä (~ riiviö|ä) | riiviö|ön | riiviö|t | riiviö|iden ~ riiviö|itten (~ riiviö|in) | riiviö|itä | riiviö|ihin |
| hupak|ko | hupak|o|n | hupak|ko|a | hupak|ko|on | hupak|o|t | hupak|ko|jen ~ hupak|o|iden ~ hupak|o|itten | hupak|ko|ja ~ hupak|o|ita | _hupak|ko|ihin ~ hupak|o|ihin_ |
| abnorm|i | abnorm|i|n | abnorm|i|a | abnorm|i|in | abnorm|i|t| abnorm|ien (~ abnorm|e|in) | abnorm|e|ja | abnorm|e|ihin |
| styd|i | styd|i|n | styd|i|ä | styd|i|in | styd|i|t | styd|ien (~ styd|e|in) | styd|e|jä | styd|e|ihin |
| opaak|ki | opaak|i|n | opaak|ki|a | opaak|ki|in | opaak|i|t | opaak|k|ien (~ opaak|ke|in) | opaak|ke|ja | opaak|ke|ihin |
| pink|ki | pink|i|n | pink|ki|ä | pink|ki|in | pink|i|t | pink|k|ien (~ pink|ke|in) | pink|ke|jä | pink|ke|ihin |
| sip|pi | sip|i|n | sip|pi|ä | sip|pi|in | sip|i|t | sip|p|ien (~ sip|pe|in) | sip|pe|jä | sip|pe|ihin |
| hurt|ti | hurt|i|n | hurt|ti|a | hurt|ti|in | hurt|i|t | hurt|t|ien (~ hurt|te|in) | hurt|te|ja | hurt|te|ihin |
| tuh|ti | tuh|di|n | tuh|ti|a | tuh|ti|in | tuh|t|ien (~ tuh|te|in) | tuh|te|ja | tuh|te|ihin |
| reh|ti | reh|di|n | reh|ti|ä | reh|ti|in | reh|t|ien (~ reh|te|in) | reh|te|jä | reh|te|ihin |
| abnormaal|i | abnormaal|i|n | abnormaal|i|a | abnormaal|i|in | abnormaal|i|t | abnormaal|ien ~ abnormaal|e|iden ~ abnormaal|e|itten (~ abnormaal|e|in) | abnormaal|e|ita ~ abnormaal|e|ja | abnormaal|e|ihin |
| toope | toope|n | toope|a | toope|en | toope|t | toope|jen (~ toope|in) | toope|ja | toope|ihin |
| aav|a | aav|a|n | aav|a|a | aav|a|an | aav|a|t | aav|o|jen (~ aav|a|in) | aav|o|ja | aav|o|ihin |
| tark|ka | tark|a|n | tark|ka|a | tark|ka|an | tark|a|t | tark|ko|jen (~ tark|ka|in) | tark|ko|ja | tark|ko|ihin |
| mat|ta | mat|a|n | mat|ta|a | mat|ta|an | mat|a|t | mat|to|jen (~ mat|ta|in) | mat|to|ja | mat|to|ihin |
| ar|ka | ar|a|n | ar|ka|a | ar|ka|an | ar|a|t | ar|ko|jen (~ ar|ka|in) | ar|ko|ja | ar|ko|ihin |
| hal|pa | hal|va|n | hal|pa|a | hal|pa|an | hal|va|t | hal|po|jen (~ hal|pa|in) | hal|po|ja | hal|po|ihin |
| eh|ta | eh|da|n | eh|ta|a | eh|ta|an | eh|da|t | eh|to|jen (~ eh|ta|in) | eh|to|ja | eh|to|ihin |
| ihan|ta | vihan|na|n | vihan|ta|a | vihan|ta|an | vihan|na|t | vihan|to|jen (~ vihan|ta|in) | vihan|to|ja | vihan|to|ihin |
| aaltoilev|a | soittaj|a|n | soittaj|a|a | soittaj|a|an | soittaj|a|t | soittaj|ien (~ soittaj|a|in) | soittaj|ia | soittaj|iin  |
| työllistettäv|| työllistettäv|ä|n | työllistettäv|ä|ä | työllistettäv|ä|än | työllistettäv|ä|t | työllistettäv|ien (~ työllistettäv|ä|in) | työllistettäv|iä | työllistettäv|iin |
| hoik|ka | hoik|a|n | hoik|ka|a | hoik|ka|an | hoik|a|t | hoik|k|ien (~ hoik|ka|in) | hoik|k|ia | hoik|k|iin  |
| myk|kä | myk|ä|n | myk|kä|ä | myk|kä|än | myk|ä|t | myk|kien (~ myk|kä|in) | myk|k|iä | myk|k|iin |
| pop|pa | pop|a|n | pop|pa|a | pop|pa|an | pop|a|t | pop|p|ien (~ pop|pa|in) | pop|p|ia | pop|p|iin  |
| hömp|pä | hömp|ä|n | hömp|pä|ä | hömp|pä|än | hömp|ä|t | hömp|pien (~ hömp|pä|in) | hömp|p|iä | hömp|p|iin |
| mär|kä | mär|ä|n | mär|kä|ä | mär|kä|än | mär|ä|t | mär|kien (~ mär|kä|in) | mär|k|iä | mär|k|iin |
| voi|pa | voi|va|n | voi|pa|a | voi|pa|an | voi|va|t | voi|p|ien (~ voi|pa|in) | voi|p|ia | voi|p|iin  |
| käy|pä | käy|vä|n | käy|pä|ä | käy|pä|än | käy|vä|t | käy|pien (~ käy|pä|in) | käy|p|iä | käy|p|iin |
| mä|tä | mä|dä|n | mä|tä|ä | mä|tä|än | mä|dä|t | mä|tien (~ mä|tä|in) | mä|t|iä | mä|t|iin |
| vän|kä | vän|gä|n | vän|kä|ä | vän|kä|än | vän|gä|t | vän|kien (~ vän|kä|in) | vän|k|iä | vän|k|iin |
| kul|ta | kul|la|n | kul|ta|a | kul|ta|an | kul|la|t | kul|t|ien (~ kul|ta|in) | kul|t|ia | kul|t|iin  |
| län|tä | län|nä|n | län|tä|ä | län|tä|än | län|nä|t | län|t|ien (~ län|tä|in) | län|t|iä | län|t|iin |
| tur|ta | tur|ra|n | tur|ta|a | tur|ta|an | tur|ra|t | tur|t|ien (~ tur|ta|in) | tur|t|ia | tur|t|iin |
| matal|a | matal|a|n | matal|a|a (~ matal|a|ta) | matal|a|an | matal|a|t | matal|ien | matal|ia | matal|iin | matal|a|mpi | matal|in |
| haper|a | haper|a|n | haper|a|a | haper|a|an | haper|a|t | haper|o|jen ~ haper|o|iden ~ haper|o|itten ~ haper|ien | haper|o|ja ~ haper|o|ita ~ haper|ia | haper|iin ~ haper|o|ihin |
| lättän|ä | lättän|ä|n | lättän|ä|ä | lättän|ä|än | lättän|ä|t | lättän|ö|jen ~ lättän|ö|iden ~ lättän|ö|itten ~ lättän|ien | lättän|ö|jä ~ lättän|ö|itä ~ lättän|iä | lättän|iin ~ lättän|ö|ihin |
| harmaj|a | harmaj|an | harmaj|aa | harmaj|aan | harmaj|at | harmaj|oiden | harmaj|oita | harmaj|oihin |
| höppän|ä | höppän|än | höppän|ää | höppän|ään | höppän|ät | höppän|öiden | höppän|öitä | höppän|öihin |
| latusk|a | latusk|an | latusk|aa | latusk|aan | latusk|at | latuskoiden ~ latuskoitten ~ latusk|ojen | latuskoita ~ latusk|oja | latusk|oihin |
| hailak|ka | hailak|an | hailak|kaa | hailak|kaan | hailak|at | hailak|oiden ~ hailak|oitten | hailak|oita | _hailak|koihin ~ hailak|oihin_ |
| räväk|kä | räväk|än | räväk|kää | räväk|kään | räväk|ät | räväk|öiden ~ räväk|öitten | räväk|öitä | _räväk|köihin ~ räväk|öihin_ |
| aino|a (~ aino|o) | aino|an | aino|a|a (~ aino|e|ta ~ aino|a|ta)| aino|a|an | aino|at | aino|iden ~ aino|itten | aino|ita | aino|isiin | ainoampi | ainoin |
| järe|ä (~ järe|e) | järe|än | järe|ä|a (~ järe|e|ta ~ järe|ä|ta)| järe|ä|an | järe|ät | järe|iden ~ järe|itten | järe|ita | järe|isiin |
| korkea | korkean | korkeaa | korkeaan | korkeat | korkeiden ~ korkeitten | korkeita | korkeisiin | korkeampi | korkein |
| aiem|pi | aiem|ma|n | aiem|pa|a | aiem|pa|an | aiem|ma|t | aiem|p|ien | aiem|p|ia | aiem|p|iin |
| lähem|pi | lähem|ma|n | lähem|pa|a | lähem|pa|an | lähem|ma|t | lähem|p|ien | lähem|p|ia | lähem|p|iin |
| vapa|a | vapa|a|n | vapa|a|ta | vapa|a|seen | vapa|a|t | vapa|iden ~ vapa|itten | vapa|ita | vapa|isiin |
| peea|a | peea|an | peea|ata | peea|ahan | peea|at | peea|iden ~ peea|itten | peea|ita | peea|ihin |
| mu|u | mu|u|n | mu|u|ta | mu|u|hun | mu|u|t | mu|iden ~ mu|itten | mu|ita | mu|ihin |
| syypä|ä | syypä|ä|n | syypä|ä|tä | syypä|ä|hän | syypä|ä|t | syypä|iden ~ syypä|itten | syypä|itä | syypä|ihin |
| suur|i | suur|en | suur|ta | suur|e|en | suur|e|t | suur|ten ~ suur|ien | suur|ia | suur|iin |
| pien|i | pien|en | pien|tä | pien|e|en | pien|e|t | pien|ten ~ pien|ien | pien|iä | pien|iin |
| uu|si | uu|de|n | uu|t|ta | uu|te|en | uu|de|t | uu|s|ien ~ uu|t|ten | uu|s|ia | uu|s|iin |
| täy|si | täy|de|n | täy|t|tä | täy|te|en | täy|de|t | täy|s|ien ~ täy|t|ten | täy|s|iä | täy|s|iin |
| tosi | toden | totta | toten | todet | tosien | tosia | tosiin |
| tyven | tyven|e|n | tyven|tä | tyven|e|en | tyven|e|t | tyven|ten | tyven|iä | tyven|iin |
| avoi|n | avoi|me|n | avoi|n|ta | avoi|me|en | avoi|me|t | avoi|n|ten | avoi|m|ia | avoi|m|iin |
| alas|ton (~ viattoin) | alas|toma|n | alas|ton|ta | alas|toma|an | alas|toma|t | alas|tom|ien | alas|tom|ia | alas|tomi|in | alas|toma|mpi | alas|tom|in |
| hap|an | hap|pama|n | hap|an|ta | hap|pama|an | hap|pama|t | hap|pam|ien | hap|pam|ia | hap|pami|in | hap|pama|mpi | hap|pam|in |
| viat|on (~ viattoin) | viat|toma|n | viat|on|ta | viat|toma|an | viat|toma|t | viat|tom|ien | viat|tom|ia | viat|tomi|in | viat|toma|mpi | viat|tom|in |
| työt|ön (~ työttöin) | työt|tömä|n | työt|ön|tä | työt|tömä|än | työt|tömä|t | työt|töm|ien | työt|töm|iä | työt|tömi|in | työt|tömä|mpi | työt|töm|in |
| läm|min | läm|pimä|n | läm|mint|ä (~ ?läm|pimä|ä) | läm|pimä|än | läm|pimä|t | läm|pim|ien | läm|pim|iä | läm|pim|iin | läm|pimä|mpi | läm|pim|in |
| pahi|n | pahi|mma|n | pahi|n|ta (~ ?pahi|mpa|a) | pahi|mpa|an | pahi|n|ten | pahi|mp|ia | pahi|mp|iin | pahi|mma|mpi | pahi|mm|in|
| sisi|n | sisi|mmä|n | sisi|n|tä (~ ?sisi|mpä|ä) | sisi|mpä|än | sisi|mmä|t | sisi|n|ten | sisi|mp|iä | sisi|mp|iin | sisi|mmä|mpi | sisi|mm|in|
| vase|n | vase|mma|n | vase|n|ta (~ vase|mpa|a) | vase|mpa|an | vase|mma|t | vase|mp|ien | vase|mp|ia | vase|mp|iin | vase|mma|mpi | vase|mm|in|
| aakkoselli|nen | aakkoselli|se|n | aakkoselli|s|ta | aakkoselli|se|en | aakkoselli|se|t | aakkoselli|s|ten ~ aakkoselli|s|ien| aakkoselli|s|ia | aakkoselli|s|iin |
| kylmäjärki|nen | kylmäjärki|se|n | kylmäjärki|s|tä | kylmäjärki|se|en | kylmäjärki|se|t | kylmäjärki|s|ten ~ kylmäjärki|s|ien| kylmäjärki|s|iä | kylmäjärki|s|iin |
| symppi|s | symppi|kse|n | symppi|s|tä | symppi|kse|en | symppi|kse|t | symppi|s|ten ~ symppi|ks|ien | symppi|ks|iä | symppi|ks|iin |
| lujatahtoisuu|s | lujatahtoisuu|de|n | lujatahtoisuu|t|ta | lujatahtoisuu|te|en | lujatahtoisuu|de|t | lujatahtoisuu|ks|ien | lujatahtoisuu|ks|ia | lujatahtoisuu|ks|iin |
| lähteisyy|s | lähteisyy|de|n | lähteisyy|t|tä | lähteisyy|te|en | lähteisyy|de|t | lähteisyy|ks|ien | lähteisyy|ks|iä | lähteisyy|ks|iin |
| autua|s | autua|a|n | autua|s|ta | autua|a|seen | autua|a|t | autua|iden | autua|ita | autua|isiin |
| työlä|s | työlä|ä|n | työlä|s|tä | työlä|ä|seen | työlä|ä|t | työlä|iden | työlä|itä | työlä|isiin |
| valmis | valmiin | valmista | valmiiseen | valmiit | valmiiden | valmiita | valmiisiin | valmiimpi | valmiin |
| voimak|as | voimak|kaa|n | voimak|as|ta | voimak|kaa|seen | voimak|kaa|t | voimak|ka|iden | voimak|ka|ita | voimak|ka|isiin |
| tyylik|äs | tyylik|kää|n | tyylik|äs|tä | tyylik|kää|seen | tyylik|kää|t | tyylik|kä|iden | tyylik|kä|ita | tyylik|kä|isiin |
| reip|as | reip|paa|n | reip|as|ta | reip|paa|seen | reip|paa|t | reip|pa|iden | reip|pa|ita | reip|pa|isiin |
| riet|as | riet|taa|n | riet|as|ta | riet|taa|seen | riet|taa|t | riet|ta|iden | riet|ta|ita | riet|ta|isiin |
| rait|is | rait|taa|n | rait|is|ta | rait|tii|seen | rait|tii|t | rait|ti|iden | rait|ti|ita | rait|ti|isiin |
| hi|das | hi|taa|n | hi|das|ta | hi|taa|seen | hi|taa|t | hi|ta|iden | hi|ta|ita | hi|ta|isiin |
| har|ras | har|taa|n | har|ras|ta | har|taa|seen | har|taa|t | har|ta|iden | har|ta|ita | har|ta|isiin |
| iäkäs | iäkkään | iäkästä | iäkkääseen | iäkkäät | iäkkäiden | iäkkäitä | iäkkäisiin | iäkkäämpi | iäkkäin |
| altis | alttiin | altista | alttiiseen | alttiit | alttiiden | alttiita | alttiisiin | alttiimpi | ?alttiin |
| ohu|t | ohu|e|n | ohu|t|ta | ohu|e|en | ohu|e|t | ohu|iden ~ ohu|itten | ohu|ita | ohu|isiin |
| ehy|t | ehy|e|n | ehy|t|tä | ehy|e|en | ehy|e|t | ehy|iden ~ ehy|itten | ehy|itä | ehy|isiin |
| kulun|ut | kulun|ee|n | kulun|ut|ta | kulun|ee|seen | kulun|ee|t | kulun|e|iden ~ kulun|e|itten | kulun|e|ita | kulun|e|isiin ~ kulun|e|ihin | kulun|eempi | kulun|ein |
| ällistyn|yt | ällistyn|ee|n | ällistyn|yt|ta | ällistyn|ee|seen | ällistyn|ee|t | ällistyn|e|iden ~ ällistyn|e|itten | ällistyn|e|ita | ällistyn|e|isiin ~ ällistyn|e|ihin | ällistyn|eempi | ällistyn|ein |
| ahne | ahne|en | ahne|tta | ahne|eseen | ahne|et | ahne|iden ~ ahne|itten | ahne|ita | ahne|isiin |
| terve | terve|en | terve|ttä | terve|eseen | terve|et | terve|iden ~ terve|itten | terve|itä | terve|isiin |

### Verb classification examples ###

The verbs are given in following forms:

  * A infinitive's singular lative - gives the _dictionary lookup form_ and the vriant of _a infinitives stem_ marked by t, d or null, and the _harmony vowel_
  * Indicative present's 1st singular - gives _weak vowel stem_
  * Indicative past's 3rd singular - gives _strong past stem_
  * Potential's 3rd singular - gives _consonant stem_ and _n assimilation_
  * Imperative 3rd singular - gives _weak consonant stem_?
  * Nut participle - gives _n assimilation class_
  * Indicative present's passive shows _passive stem_ marked by allomorphs t variant

| A inf. sg. lat. | Ind. pres. 1st sg. | Ind. past 3rd sg. | Pot. 3rd sg. | Imp. 3rd sg. | Nut participle | Ind. pres. passive |
|:----------------|:-------------------|:------------------|:-------------|:-------------|:---------------|:-------------------|
| kaunistu|a | kaunistu|n | kaunistu|i | kaunistu|nee | kaunistu|koon | kaunistu|nut | kaunistu|ttiin |
| puno|a | puno|n | puno|i | puno|isi | puno|nee | puno|koon | puno|nut | puno|ttiin |
| ällisty|ä | ällisty|n | ällisty|i | ällisty|nee | ällisty|köön | ällisty|nyt | ällisty|ttiin |
| nuok|ku|a | nuok|u|n | nuok|ku|i | nuok|ku|nee | nuok|ku|koon | nuok|ku|nut | nuok|u|ttiin |
| kärk|ky|ä | kärk|y|n | kärk|ky|i | kärk|ky|nee | kärk|ky|köön | kärk|ky|nyt | kärk|y|ttiin |
| harp|po|a | harp|u|n | harp|po|i | harp|po|nee | harp|po|koon | harp|po|nut | harp|u|ttiin |
| lop|pu|a | lop|u|n | lop|pu|i | lop|pu|nee | lop|pu|koon | lop|pu|nut | lop|u|ttiin |
| lep|py|ä | lep|y|n | lep|py|i | lep|py|nee | lep|py|köön | lep|py|nyt | lep|y|ttiin |
| hermot|tu|a | hermot|u|n | hermot|tu|i | hermot|tu|nee | hermot|tu|koon | hermot|tu|nut | hermot|u|ttiin |
| kivet|ty|ä | kivet|y|n | kivet|ty|i | kivet|ty|nee | kivet|ty|köön | kivet|ty|nyt | kivet|y|ttiin |
| mau|ku|a | mau|’u|n | mau|ku|i | mau|ku|nee | mau|ku|koon | mau|ku|nut | mau|’u|ttiin |
| ta|ko|a | ta|o|n (~ ta|’o|n) | ta|ko|i | ta|ko|nee | ta|ko|koon | ta|ko|nut | ta|o|ttiin (~ ta|’o|ttiin) |
| mäi|ky|ä | mäi|y|n | mäi|ky|i | mäi|ky|nee | mäi|ky|köön | mäi|ky|nyt | mäi|y|ttiin |
| sil|po|a | sil|vo|n | sil|po|i | sil|po|nee | sil|po|poon | sil|po|nut | sil|vo|ttiin |
| hii|pu|a | hii|vu|n | hii|pu|i | hii|pu|nee | hii|pu|koon | hii|pu|nut | hii|vu|ttiin |
| el|py|ä | el|vy|n | el|py|i | el|py|nee | el|py|köön | el|py|nyt | el|vy|ttiin |
| kie|to|a | kie|do|n | kie|to|i | kie|to|nee | kie|to|toon | kie|to|nut | kie|do|ttiin |
| roh|tu|a | roh|du|n | roh|tu|i | roh|tu|nee | roh|tu|koon | roh|tu|nut | roh|du|ttiin |
| siliy|ty|ä | siliy|dy|n | siliy|ty|i | siliy|ty|nee | siliy|ty|köön | siliy|ty|nyt | siliy|dy|ttiin |
| pen|ko|a | pen|go|n | pen|ko|i | pen|ko|nee | pen|ko|koon | pen|ko|nut | pen|go|ttiin |
| vin|ku|a | vin|gu|n | vin|ku|i | vin|ku|nee | vin|ku|koon | vin|ku|nut | vin|gu|ttiin |
| tem|po|a | tem|mo|n | tem|po|i | tem|po|nee | tem|po|poon | tem|po|nut | tem|mo|ttiin |
| am|pu|a | am|mu|n | am|pu|i | am|pu|nee | am|pu|koon | am|pu|nut | am|mu|ttiin |
| humal|tu|a | humal|lu|n | humal|tu|i | humal|tu|nee | humal|tu|koon | humal|tu|nut | humal|lu|ttiin |
| miel|ty|ä | miel|ly|n | miel|ty|i | miel|ty|nee | miel|ty|köön | miel|ty|nyt | miel|ly|ttiin |
| vakaan|tu|a | vakaan|nu|n | vakaan|tu|i | vakaan|tu|nee | vakaan|tu|koon | vakaan|tu|nut | vakaan|nu|ttiin |
| tyhjen|ty|ä | tyhjen|ny|n | tyhjen|ty|i | tyhjen|ty|nee | tyhjen|ty|köön | tyhjen|ty|nyt | tyhjen|ny|ttiin |
| puser|tu|a | puser|ru|n | puser|tu|i | puser|tu|nee | puser|tu|koon | puser|tu|rut | puser|ru|ttiin |
| pyör|ty|ä | pyör|ry|n | pyör|ty|i | pyör|ty|nee | pyör|ty|köön | pyör|ty|ryt | pyör|ry|ttiin |
| mutrist|aa | mutrist|a|n | mutrist|i | mutrist|a|isi | mutrist|a|nee | mutrist|a|koon | mutrist|a|nut | mutrist|e|ttiin |
| kivist|ää | kivist|ä|n | kivist|i | kivist|ä|isi | kivist|ä|nee | kivist|ä|köön | kivist|ä|nyt | kivist|e|ttiin |
| vieroit|taa | vieroit|a|n | vieroit|t|i | vieroit|ta|isi | vieroit|ta|nee | vieroit|ta|koon | vieroit|ta|nut | vieroit|e|ttiin |
| räpsyt|tää | räpsyt|tä|n | räpsyt|ti | räpsyt|tä|isi | räpsyt|tä|nee | räpsyt|tä|köön | räpsyt|tä|nyt | räpsyt|te|ttiin |
| pur|kaa | pur|a|n | pur|k|i | pur|ka|isi | pur|ka|nee | pur|ka|koon | pur|ka|nut | pur|e|ttiin |
| mojah|taa | mojah|da|n | mojah|t|i | mojah|ta|isi | mojah|ta|nee | mojah|ta|koon | mojah|ta|nut | mojah|de|ttiin |
| kyn|tää | kyn|nä|n | kyn|ti | kyn|tä|isi | kyn|tä|nee | kyn|tä|köön | kyn|tä|nyt | kyn|ne|ttiin |
| sor|taa | sor|ra|n | sor|t|i | sor|ta|isi | sor|ta|nee | sor|ta|koon | sor|ta|nut | sor|re|ttiin |
| hidastaa | hidastan | hidasti | hidastaisi | hidastanee | hidastakoon | hidastanut | hidastettiin |
| loistaa | loistan | loisti | loistaisi | loistanee | loistakoon | loistanut | loistettiin |
| kirjoittaa | kirjoitan | kirjoitti | kirjoittaisi | kirjoittanee | kirjoittakoon | kirjoittanut | kirjoitettiin |
| heittää | heitän | heitti | heittäisi | heittänee | heittäköön | heittänyt | heitettiin |
| inttää | intän | intti | inttäisi | inttänee | inttäköön | inttänyt | intettiin |
| sulaa | sulan | suli | sulaisi | sulanee | sulakoon | sulanut | sulettiin |
| hohtaa | hohdan | hohti | hohtaisi | hohtanee | hohtakoon | hohtanut | hohdettiin |
| hujahtaa | hujahdan | hujahti | hujahtaisi | hujahtanee | hujahtakoon | hujahtanut | hujahdettiin |
| vuo|ta|a | vuo|da|n | vuo|s|i ~ vuo|t|i | vuo|ta|isi | vuo|ta|nee | vuo|ta|koon | vuo|ta|nut | vuo|de|ttiin |
| XX huu|ta|a| huu|da|n | huu|s|i (~ huu|t|i) | huu|ta|isi | huu|ta|nee | huu|ta|koon | huu|ta|nut | huu|de|ttiin |
| pyy|tä|ä | pyy|dä|n | pyy|s|i (~ pyy|t|i) | pyy|tä|isi | pyy|tä|nee | pyy|tä|koon | pyy|tä|nyt | pyy|de|ttiin |
| sival|ta|a | sival|la|n | sival|s|i (~ sival|t|i) | sival|ta|isi | sival|ta|nee | sival|ta|koon | sival|ta|nut | sival|le|ttiin |
| vihel|tä|ä | vihel|lä|n | vihel|s|i (~ vihel|t|i) | vihel|tä|isi | vihel|tä|nee | vihel|tä|koon | vihel|tä|nyt | vihel|le|ttiin |
| huonon|ta|a | huonon|na|n | huonon|s|i (~ huonon|t|i) | huonon|ta|isi | huonon|ta|nee | huonon|ta|koon | huonon|ta|nut | huonon|ne|ttiin |
| hiven|tä|ä | hiven|nä|n | hiven|s|i (~ hiven|t|i) | hiven|tä|isi | hiven|tä|nee | hiven|tä|koon | hiven|tä|nyt | hiven|ne|ttiin |
| kuher|ta|a | kuher|ra|r | kuher|s|i (~ kuher|t|i) | kuher|ta|isi | kuher|ta|nee | kuher|ta|koon | kuher|ta|rut | kuher|re|ttiin |
| näper|tä|ä | näper|rä|r | näper|s|i (~ näper|t|i) | näper|tä|isi | näper|tä|nee | näper|tä|koon | näper|tä|ryt | näper|re|ttiin |
| paleltaa | palellan | palelsi | paleltaisi | paleltanee | paleltakoon | paleltanut | palellettiin |
| sukeltaa | sukellan | sukelsi | sukeltaisi | sukeltanee | sukeltakoon | sukeltanut | sukellettiin |
| juontaa | juonnan | juonsi | juontaisi | juontanee | juontakoon | juontanut | juonnettiin |
| pahentaa | pahennan | pahensi | pahentaisi | pahentanee | pahentakoon | pahennettiin |
| murtaa | murran | mursi | murtaisi | murtanee | murtakoon | murtanut | murrettiin |
| sortaa | sorran | sorti | sortaisi | sortanee | sortakoon | sortanut | sorrettiin |
| sou|ta|a | sou|da|n | sou|t|i ~ sou|s|i | sou|ta|isi | sout|a|nee | sou|ta|koon | sou|ta|nut | sou|de|ttiin |
| kii|tä|ä | kii|dä|n | kii|t|i ~ kii|s|i | kii|tä|isi | sout|ä|nee | kii|tä|köön | kii|tä|nyt | kii|de|ttiin |
| yl|tä|ä | yl|lä|n | yl|t|i ~ yl|s|i | yl|tä|isi | sout|ä|nee | yl|tä|köön | yl|tä|nyt | yl|le|ttiin |
| en|tä|ä | en|nä|n | en|t|i ~ en|s|i | en|tä|isi | sout|ä|nee | en|tä|köön | en|tä|nyt | en|ne|ttiin |
| kasv|a|a | kasv|a|n | kasv|o|i | kasv|a|isi | kasv|a|nee | kasv|a|koon | kasv|a|nut | kasv|e|ttiin |
| virk|ka|a | virk|a|n | virk|ko|i | virk|ka|isi | virk|ka|nee | virk|ka|koon | virk|ka|nut | virk|e|ttiin |
| tap|pa|a | tap|a|n | tap|po|i | tap|pa|isi | tap|pa|nee | tap|pa|poon | tap|pa|nut | tap|e|ttiin |
| ja|ka|a | ja|a|n | ja|ko|i | ja|ka|isi | ja|ka|nee | ja|ka|koon | ja|ka|nut | ja|e|ttiin |
| sa|ta|a | sa|da|n | sa|to|i | sa|ta|isi | sa|ta|nee | sa|ta|koon | sa|ta|nut | sa|de|ttiin |
| kan|ta|a | kan|na|n | kan|to|i | kan|ta|isi | kan|ta|nee | kan|ta|koon | kan|ta|nut | kan|ne|ttiin |
| kaivaa | kaivan | kaivoi | kaivaisi | kaivanee | kaivakoon | kaivanut | kaivettiin |
| haastaa | haastan | haastoi | haastaisi | haastanee | haastakoon | haastanut | haastettiin |
| paistaa | paistan | paistoi | paistaisi | paistanee | paistakoon | paistanut | paistettiin |
| palaa | palan | paloi | palaisi | palanee | palakoon | palanut | palettiin |
| virkkaa | virkan | virkkoi | virkkaisi | virkkanee | virkkakoon | virkkanut | virkettiin |
| laittaa | laitan | laittoi | laittaisi | laittanee | laittakoon | laittanut | laitettiin |
| taittaa | taitan | taittoi | taittaisi | taittanee | taittakoon | taittanut | taitettiin |
| kaihtaa | kaihdan | kaihtoi | kaihtaisi | kaihtanee | kaihtakoon | kaihtanut | kaihdettiin |
| paahtaa | paahdan | paahtoi | paahtaisi | paahtanee | paahtakoon | paahtanut | paahdettiin |
| kaa|ta|a | kaa|da|n | kaa|s|i ~ kaa|to|i | kaa|ta|isi | kaa|ta|nee | kaa|ta|koon | kaa|ta|nut | kaa|de|ttiin |
| saar|taa | saar|ra|n | saar|s|i ~ saar|to|i | saar|ta|isi | saar|ta|nee | saar|ta|koon | saar|ta|nut | saar|re|ttiin |
| sotk|e|a | sotk|e|n | sotk|i | sotk|isi | sotk|e|nee | sotk|e|koon | sotk|e|nut | sotk|e|ttiin |
| kytk|e|ä | kytk|e|n | kytk|i | kytk|isi | kytk|e|nee | kytk|e|köön | kytk|e|nyt | kytk|e|ttiin |
| pu|ke|a | pu|e|n | pu|ki | pu|k|isi | pu|ke|nee | pu|ke|koon | pu|ke|nut | pu|e|ttiin |
| ry|pe|ä | ry|ve|n | ry|pi | ry|p|isi | ry|pe|nee | ry|pe|köön | ry|pe|nyt | ry|ve|ttiin |
| ku|te|a | ku|de|n | ku|ti | ku|t|isi | ku|te|nee | ku|te|koon | ku|te|nut | ku|de|ttiin |
| pä|te|ä | pä|de|n | pä|ti | pä|t|isi | pä|te|nee | pä|te|köön | pä|te|nyt | pä|de|ttiin |
| tun|ke|a | tun|ge|n | tun|ki | tun|k|isi | tun|ke|nee | tun|ke|koon | tun|ke|nut | tun|ge|ttiin |
| pol|ke|a | pol|je|n | pol|ki | pol|k|isi | pol|ke|nee | pol|ke|koon | pol|ke|nut | pol|je|ttiin |
| sär|ke|ä | sär|je|n | sär|ti | sär|k|isi | sär|ke|nee | sär|ke|köön | sär|ke|nyt | sär|je|ttiin |
| potea | poden | poti (~ posi) | potisi | potekoon | potenut | podettiin |
| tun|te|a | tun|ne|n | tun|s|i | tun|t|isi | tun|te|nee | tun|te|koon | tun|te|nut | tun|ne|ttiin |
| lä|hte|ä | lä|hde|n | lä|ht|i ~ lä|ks|i | lä|ht|isi ~ lä|ks|isi | lä|ht|enee | lä|hte|köön | lä|hte|nyt | lä|hde|ttiin |
| kos|i|a | kos|i|n | kos|i | kos|isi | kos|i|nee | kos|i|koon | kos|i|nut |kos|i|ttiin |
| rysk|i|ä | rysk|i|n | rysk|i | rysk|isi | rysk|i|nee | rysk|i|köön | rysk|i|nyt |rysk|i|ttiin |
| kuk|ki|a | kuk|i|n | kuk|ki | kuk|k|isi | kuk|ki|nee | kuk|ki|koon | kuk|ki|nut |kuk|i|ttiin |
| sörk|ki|ä | sörk|i|n | sörk|k|i | sörk|k|isi | sörk|ki|nee | sörk|ki|köön | sörk|ki|nyt |sörk|i|ttiin |
| kalp|pi|a | kalp|i|n | kalp|pi | kalp|p|isi | kalp|pi|nee | kalp|pi|koon | kalp|pi|nut |kalp|i|ttiin |
| hyp|pi|ä | hyp|i|n | hyp|k|i | hyp|p|isi | hyp|pi|nee | hyp|pi|köön | hyp|pi|nyt |hyp|i|ttiin |
| moit|ti|a | moit|i|n | moit|ti | moit|t|isi | moit|ti|nee | moit|ti|koon | moit|ti|nut |moit|i|ttiin |
| miet|ti|ä | miet|i|n | miet|k|i | miet|t|isi | miet|ti|nee | miet|ti|köön | miet|ti|nyt |miet|i|ttiin |
| su|ki|a | su|i|n | su|ki | su|k|isi | su|ki|nee | su|ki|koon | su|ki|nut |su|i|ttiin |
| mää|ki|ä | mää|i|n | mää|k|i | mää|k|isi | mää|ki|nee | mää|ki|köön | mää|ki|nyt |mää|i|ttiin |
| raa|pi|a | raa|vi|n | raa|pi | raa|p|isi | raa|pi|nee | raa|pi|koon | raa|pi|nut |raa|vi|ttiin |
| rii|pi|ä | rii|vi|n | rii|k|vi | rii|p|isi | rii|pi|nee | rii|pi|köön | rii|pi|nyt |rii|vi|ttiin |
| ahneh|ti|a | ahneh|di|n | ahneh|ti | ahneh|t|isi | ahneh|ti|nee | ahneh|ti|koon | ahneh|ti|nut |ahneh|di|ttiin |
| eh|ti|ä | eh|di|n | eh|k|di | eh|t|isi | eh|ti|nee | eh|ti|köön | eh|ti|nyt |eh|di|ttiin |
| on|ki|a | on|gi|n | on|ki | on|k|isi | on|ki|nee | on|ki|koon | on|ki|nut |on|gi|ttiin |
| mön|ki|ä | mön|gi|n | mön|k|gi | mön|k|isi | mön|ki|nee | mön|ki|köön | mön|ki|nyt |mön|gi|ttiin |
| tym|pi|ä | tym|mi|n | tym|p|mi | tym|p|isi | tym|pi|nee | tym|pi|köön | tym|pi|nyt |tym|mi|ttiin |
| kon|ti|a | kon|ni|n | kon|ti | kon|t|isi | kon|ti|nee | kon|ti|tokon | kon|ti|nut |kon|ni|ttiin |
| hyl|ki|ä | hyl|ji|n | hyl|k|ji | hyl|k|isi | hyl|ki|nee | hyl|ki|köön | hyl|ki|nyt |hyl|ji|ttiin |
| kopio|ida | kopio|i|n | kopio|i | kopio|isi | kopio|i|nee | kopio|i|koon | kopio|i|nut | kopio|i|tiin |
| voida | voin | voi | voisi | voinee | voinut | voitiin |
| naida | nain | nai | naisi | nainee | nainut | naitiin |
| sa|a|da | sa|a|n | sa|i | sa|isi | sa|a|nee | sa|a|koon | sa|a|nut | sa|a|tiin |
| my|y|dä | my|y|n | my|i | my|isi | my|y|nee | my|y|köön | my|y|nyt | my|y|tiin |
| jä|ä|dä | jä|ä|n | jä|i | jä|isi | jä|ä|nee | jä|ä|köön | jä|ä|nyt | jä|ä|tiin |
| t|uo|da | t|uo|n | t|o|i | t|o|isi | t|uo|nee | t|uo|koon | t|uo|nut | t|uo|tiin |
| v|ie|dä | v|ie|n | v|e|i | v|e|isi | v|ie|nee | v|ie|köön | v|ie|nyt | v|ie|tiin |
| s|yö|dä | s|yö|n | s|ö|i | s|ö|isi | s|yö|nee | s|yö|köön | s|yö|nyt | s|yö|tiin |
| kä|y|dä | kä|y|n | kä|v|i | kä|v|isi | kä|y|nee | kä|y|köön | kä|y|nyt | kä|y|tiin |
| maris|ta | maris|e|n | maris|i | maris|see | maris|koot | maris|sut | maris|tiin |
| hä|väis|tä | hä|päise|n | hä|pä|isi | hä|väis|see | hä|väis|kööt | hä|väis|syt | hä|päis|tiin |
| va|vis|ta | va|pise|n | va|p|isi | va|vis|see | va|vis|koot | va|vis|sut | va|pis|tiin |
| ran|gais|ta | ran|kaise|n | ran|ka|isi | ran|gais|see | ran|gais|koot | ran|gais|sut | ran|kais|tiin |
| kihistä | kihisen (~ kihajan) | kihisi (~ kihaji) | kihisisi ~ kihajaisi | kihissee | kihissyt | kihistiin |
| kitistä | kitisen | kitisi | kitissee | kitissyt | kitistiin |
| vastail|la | vastail|en | vastail|i | vastail|isi | vastail|lee | vastail|koot | vastail|lut | vastail|tiin |
| XX purra| puren | puri | purisi | purree | purrut | purtiin |
| XX mennä| menen | meni | menisi | mennee | mennyt | mentiin |
| nak|el|la | nak|kele|n | nak|kel|i | nak|kel|isi | nak|el|lee | nak|el|koot | nak|el|lut | nak|el|tiin |
| tap|el|la | tap|pele|n | tap|pel|i | tap|pel|isi | tap|el|lee | tap|el|koot | tap|el|lut | tap|el|tiin |
| hyp|el|lä | hyp|pele|n | hyp|pel|i | hyp|pel|isi | hyp|el|lee | hyp|el|kööt | hyp|el|lyt | hyp|el|tiin |
| sulat|el|la | sulat|tele|n | sulat|tel|i | sulat|tel|isi | sulat|el|lee | sulat|el|koot | sulat|el|lut | sulat|el|tiin |
| herät|el|lä | herät|tele|n | herät|tel|i | herät|tel|isi | herät|el|lee | herät|el|kööt | herät|el|lyt | herät|el|tiin |
| ja|el|la | ja|kele|n | ja|kel|i | ja|kel|isi | ja|el|lee | ja|el|koot | ja|el|lut | ja|el|tiin |
| tipah|del|la | tipah|tele|n | tipah|tel|i | tipah|tel|isi | tipah|del|lee | tipah|del|koot | tipah|del|lut | tipah|del|tiin |
| säpsäh|del|lä | säpsäh|tele|n | säpsäh|tel|i | säpsäh|tel|isi | säpsäh|del|lee | säpsäh|del|kööt | säpsäh|del|lyt | säpsäh|del|tiin |
| om|mel|la | om|pele|n | om|pel|i | om|pel|isi | om|mel|lee | om|mel|koot | om|mel|lut | om|mel|tiin |
| vael|lel|la | vael|tele|n | vael|tel|i | vael|tel|isi | vael|lel|lee | vael|lel|koot | vael|lel|lut | vael|lel|tiin |
| kiil|lel|lä | kiil|tele|n | kiil|tel|i | kiil|tel|isi | kiil|lel|lee | kiil|lel|kööt | kiil|lel|lyt | kiil|lel|tiin |
| komen|nel|la | komen|tele|n | komen|tel|i | komen|tel|isi | komen|nel|lee | komen|nel|koot | komen|nel|lut | komen|nel|tiin |
| kään|nel|lä | kään|tele|n | kään|tel|i | kään|tel|isi | kään|nel|lee | kään|nel|kööt | kään|nel|lyt | kään|nel|tiin |
| naker|rel|la | naker|tele|r | naker|tel|i | naker|tel|isi | naker|rel|lee | naker|rel|koot | naker|rel|lut | naker|rel|tiin |
| kiher|rel|lä | kiher|tele|r | kiher|tel|i | kiher|tel|isi | kiher|rel|lee | kiher|rel|kööt | kiher|rel|lyt | kiher|rel|tiin |
| kirjoitella | kirjoittelen | kirjoitteli | kirjoittelisi | kirjoitellee | kirjoitellut | kirjoiteltiin |
| ol|la | ol|e|n | ol|i | ol|isi | _lienee_ | ol|koot | ol|lut | ol|tiin |
| rvailla ~ arvaella | arvailen | arvaili | arvailisi | arvaillee | arvaillut | arvailtiin |
| mellako|i|da | mellako|i|n ~ mellako|itse|n  | mellako|i ~ mellako|itsi  | mellako|isi ~ mellako|its|isi | mellako|i|nee | mellako|i|koot | mellako|i|nut | mellako|i|tiin |
| isännö|i|dä | isännö|i|n ~ isännö|itse|n  | isännö|i ~ isännö|itsi  | isännö|isi ~ isännö|its|isi | isännö|i|nee | isännö|i|kööt | isännö|i|nyt | isännö|i|tiin |
| palki|ta | palki|tse|n | palki|ts|i | palki|ts|isi | palki|n|nee | palki|t|koot | palki|n|nut | palki|t|tiin |
| merki|tä | merki|tse|n | merki|ts|i | merki|ts|isi | merki|n|nee | merki|t|kööt | merki|n|nyt | merki|t|tiin |
| kudita| kutian | kutisi | kutiaisi | kudinnee | kudinnut | kudittiin |
| juo|s|ta | juo|kse|n | juo|ks|i | juo|ks|isi | juo|s|see | juo|s|koot | juo|s|sut | juo|s|tiin |
| pie|s|tä | pie|kse|n | pie|ks|i | pie|ks|isi | pie|s|see | pie|s|kööt | pie|s|syt | pie|s|tiin |
| nä|h|dä | nä|e|n | nä|k|i | nä|k|isi | nä|h|nee | nä|h|kööt | nä|h|nyt | nä|h|tiin |
| karhe|ta | karhe|ne|n | karhe|n|i | karhe|n|isi | karhe|n|nee | karhe|t|koot | karhe|n|nut | karhe|t|tiin |
| niuk|e|ta | niuk|kene|n | niuk|ken|i | niuk|ken|isi | niuk|en|nee | niuk|et|koot | niuk|en|nut | niuk|et|tiin |
| jyrk|e|tä | jyrk|kene|n | jyrk|ken|i | jyrk|ken|isi | jyrk|en|nee | jyrk|et|kööt | jyrk|en|nyt | jyrk|et|tiin |
| hap|a|ta | hap|pane|n | hap|pan|i | hap|pan|isi | hap|an|nee | hap|at|koot | hap|an|nut | hap|at|tiin |
| sup|e|ta | sup|pene|n | sup|pen|i | sup|pen|isi | sup|en|nee | sup|et|koot | sup|en|nut | sup|et|tiin |
| tylp|e|tä | tylp|pene|n | tylp|pen|i | tylp|pen|isi | tylp|en|nee | tylp|et|pööt | tylp|en|nyt | tylp|et|tiin |
| help|o|ta | help|pone|n | help|pon|i | help|pon|isi | help|on|nee | help|ot|koot | help|on|nut | help|ot|tiin |
| loit|o|ta | loit|tone|n | loit|ton|i | loit|ton|isi | loit|on|nee | loit|ot|koot | loit|on|nut | loit|ot|tiin |
| to|e|ta | to|kene|n | to|ken|i | to|ken|isi | to|en|nee | to|et|koot | to|en|nut | to|et|tiin |
| ky|e|tä | ky|kene|n | ky|ken|i | ky|ken|isi | ky|en|nee | ky|et|pööt | ky|en|nyt | ky|et|tiin |
| ul|o|ta | ul|kone|n | ul|kon|i | ul|kon|isi | ul|on|nee | ul|ot|koot | ul|on|nut | ul|ot|tiin |
| ka|ve|ta | ka|pene|n | ka|pen|i | ka|pen|isi | ka|ven|nee | ka|vet|koot | ka|ven|nut | ka|vet|tiin |
| leu|do|ta | leu|tone|n | leu|ton|i | leu|ton|isi | leu|don|nee | leu|dot|koot | leu|don|nut | leu|dot|tiin |
| pi|de|tä | pi|tene|n | pi|ten|i | pi|ten|isi | pi|den|nee | pi|det|pööt | pi|den|nyt | pi|det|tiin |
| mä|dä|tä | mä|täne|n | mä|tän|i | mä|tän|isi | mä|dän|nee | mä|dät|pööt | mä|dän|nyt | mä|dät|tiin |
| kiin|ne|tä | kiin|tene|n | kiin|ten|i | kiin|ten|isi | kiin|nen|nee | kiin|net|pööt | kiin|nen|nyt | kiin|net|tiin |
| jul|je|ta | jul|kene|n | jul|ken|i | jul|ken|isi | jul|jen|nee | jul|jet|koot | jul|jen|nut | jul|jet|tiin |
| il|je|tä | il|kene|n | il|ken|i | il|ken|isi | il|jen|nee | il|jet|kööt | il|jen|nyt | il|jet|tiin |
| arva|ta | arva|a|n | arva|s|i | arva|isi | arva|n|nee | arva|t|koot | arva|n|nut | arva|t|tiin |
| mork|a|ta | mork|kaa|n | mork|kas|i | mork|ka|isi | mork|an|nee | mork|at|koot | mork|an|nut | mork|at|tiin |
| siep|a|ta | siep|paa|n | siep|pas|i | siep|pa|isi | siep|an|nee | siep|at|koot | siep|an|nut | siep|at|tiin |
| välp|ä|tä | välp|pää|n | välp|päs|i | välp|pä|isi | välp|än|nee | välp|ät|kööt | välp|än|nyt | välp|ät|tiin |
| lunt|a|ta | lunt|taa|n | lunt|tas|i | lunt|ta|isi | lunt|an|nee | lunt|at|koot | lunt|an|nut | lunt|at|tiin |
| länt|ä|tä | länt|tää|n | länt|täs|i | länt|tä|isi | länt|än|nee | länt|ät|kööt | länt|än|nyt | länt|ät|tiin |
| li|a|ta | li|kaa|n | li|kas|i | li|ka|isi | li|an|nee | li|at|koot | li|an|nut | li|at|tiin |
| hyl|ä|tä | hyl|kää|n | hyl|käs|i | hyl|kä|isi | hyl|än|nee | hyl|ät|kööt | hyl|än|nyt | hyl|ät|tiin |
| kai|va|ta | kai|paa|n | kai|pas|i | kai|pa|isi | kai|van|nee | kai|vat|koot | kai|van|nut | kai|vat|tiin |
| le|vä|tä | le|pää|n | le|päs|i | le|pä|isi | le|vän|nee | le|vät|kööt | le|vän|nyt | le|vät|tiin |
| jah|da|ta | jah|taa|n | jah|tas|i | jah|ta|isi | jah|dan|nee | jah|dat|koot | jah|dan|nut | jah|dat|tiin |
| täh|dä|tä | täh|tää|n | täh|täs|i | täh|tä|isi | täh|dän|nee | täh|dät|kööt | täh|dän|nyt | täh|dät|tiin |
| von|ga|ta | von|kaa|n | von|kas|i | von|ka|isi | von|gan|nee | von|gat|koot | von|gan|nut | von|gat|tiin |
| vän|gä|tä | vän|pää|n | vän|päs|i | vän|pä|isi | vän|gän|nee | vän|gät|kööt | vän|gän|nyt | vän|gät|tiin |
| tem|ma|ta | tem|paa|n | tem|pas|i | tem|pa|isi | tem|man|nee | tem|mat|koot | tem|man|nut | tem|mat|tiin |
| mul|la|ta | mul|taa|n | mul|tas|i | mul|ta|isi | mul|lan|nee | mul|lat|koot | mul|lan|nut | mul|lat|tiin |
| suun|na|ta | suun|taa|n | suun|tas|i | suun|ta|isi | suun|nan|nee | suun|nat|koot | suun|nan|nut | suun|nat|tiin |
| ryn|nä|tä | ryn|tää|n | ryn|täs|i | ryn|tä|isi | ryn|nän|nee | ryn|nät|kööt | ryn|nän|nyt | ryn|nät|tiin |
| vir|ra|ta | vir|taa|r | vir|tas|i | vir|ta|isi | vir|ran|ree | vir|rat|koot | vir|ran|rut | vir|rat|tiin |
| hyl|jä|tä | hyl|kää|n | hyl|käs|i | hyl|kä|isi | hyl|jän|nee | hyl|jät|kööt | hyl|jän|nyt | hyl|jät|tiin |
| lob|a|ta | lob|baa|n | lob|bas|i | lob|ba|isi | lob|an|ee | lob|at|koot | lob|an|nut | lob|at|tiin |
| dig|a|ta | dig|gaa|n | dig|gas|i | dig|ga|isi | dig|an|ee | dig|at|koot | dig|an|nut | dig|at|tiin |
| saneerata | saneeraan | saneerasi | saneeraisi | saneerannee | saneerannut | saneerattiin |
| palata | palaan (~ palajan) | palasi | palaisi | palannee | palannut | palattiin |
| karhu|ta | karhu|a|n | karhu|si | karhu|a|isi (~ karhu|isi) | karhu|n|nee | karhu|t|koot | karhu|n|nut | karhu|t|tiin |
| tähy|tä | tähy|ä|n | tähy|s|i | tähy|ä|isi (~ tähy|isi) | tähy|n|nee | tähy|t|kööt | tähy|n|nyt | tähy|t|tiin |
| poik|e|ta | poik|kea|n | poik|kes|i | poik|kea|isi (~ poik|keisi) | poik|en|nee | poik|et|koot | poik|en|nut | poik|et|tiin |
| kaik|o|ta | kaik|koa|n | kaik|kos|i | kaik|koa|isi (~ kaik|koisi) | kaik|on|nee | kaik|ot|koot | kaik|on|nut | kaik|ot|tiin |
| kouk|u|ta | kouk|kua|n | kouk|kus|i | kouk|kua|isi (~ kouk|kuisi) | kouk|un|nee | kouk|ut|koot | kouk|un|nut | kouk|ut|tiin |
| up|o|ta | up|poa|n | up|pos|i | up|poa|isi (~ up|poisi) | up|on|nee | up|ot|koot | up|on|nut | up|ot|tiin |
| pulp|u|ta | pulp|pua|n | pulp|pus|i | pulp|pua|isi (~ pulp|puisi) | pulp|un|nee | pulp|ut|koot | pulp|un|nut | pulp|ut|tiin |
| luut|u|ta | luut|tua|n | luut|tus|i | luut|tua|isi (~ luut|tuisi) | luut|un|nee | luut|ut|koot | luut|un|nut | luut|ut|tiin |
| no|e|ta | no|kea|n | no|kes|i | no|kea|isi (~ no|keisi) | no|en|nee | no|et|koot | no|en|nut | no|et|tiin |
| ker|e|tä | ker|keä|n | ker|kes|i | ker|keä|isi (~ ker|keisi) | ker|en|nee | ker|et|kööt | ker|en|nyt | ker|et|tiin |
| se|o|ta | se|koa|n | se|kos|i | se|koa|isi (~ se|koisi) | se|on|nee | se|ot|koot | se|on|nut | se|ot|tiin |
| kor|ve|ta | kor|pea|n | kor|pes|i | kor|pea|isi (~ kor|peisi) | kor|ven|nee | kor|vet|koot | kor|ven|nut | kor|vet|tiin |
| re|ve|tä | re|peä|n | re|pes|i | re|peä|isi (~ re|peisi) | re|ven|nee | re|vet|kööt | re|ven|nyt | re|vet|tiin |
| kir|vo|ta | kir|poa|n | kir|pos|i | kir|poa|isi (~ kir|poisi) | kir|von|nee | kir|vot|koot | kir|von|nut | kir|vot|tiin |
| ki|vu|ta | ki|pua|n | ki|pus|i | ki|pua|isi (~ ki|puisi) | ki|vun|nee | ki|vut|koot | ki|vun|nut | ki|vut|tiin |
| to|de|ta | to|tea|n | to|tes|i | to|tea|isi (~ to|teisi) | to|den|nee | to|det|koot | to|den|nut | to|det|tiin |
| vyyh|de|tä | vyyh|teä|n | vyyh|tes|i | vyyh|teä|isi (~ vyyh|teisi) | vyyh|den|nee | vyyh|det|kööt | vyyh|den|nyt | vyyh|det|tiin |
| ka|do|ta | ka|toa|n | ka|tos|i | ka|toa|isi (~ ka|toisi) | ka|don|nee | ka|dot|koot | ka|don|nut | ka|dot|tiin |
| lii|du|ta | lii|tua|n | lii|tus|i | lii|tua|isi (~ lii|tuisi) | lii|dun|nee | lii|dut|koot | lii|dun|nut | lii|dut|tiin |
| tun|ge|ta | tun|kea|n | tun|kes|i | tun|kea|isi (~ tun|keisi) | tun|gen|nee | tun|get|koot | tun|gen|nut | tun|get|tiin |
| än|ge|tä | än|keä|n | än|kes|i | än|keä|isi (~ än|keisi) | än|gen|nee | än|get|kööt | än|gen|nyt | än|get|tiin |
| pin|go|ta | pin|koa|n | pin|kos|i | pin|koa|isi (~ pin|koisi) | pin|gon|nee | pin|got|koot | pin|gon|nut | pin|got|tiin |
| kam|me|ta | kam|pea|n | kam|pes|i | kam|pea|isi (~ kam|peisi) | kam|men|nee | kam|met|koot | kam|men|nut | kam|met|tiin |
| sam|mo|ta | sam|poa|n | sam|pos|i | sam|poa|isi (~ sam|poisi) | sam|mon|nee | sam|mot|koot | sam|mon|nut | sam|mot|tiin |
| kum|mu|ta | kum|pua|n | kum|pus|i | kum|pua|isi (~ kum|puisi) | kum|mun|nee | kum|mut|koot | kum|mun|nut | kum|mut|tiin |
| in|no|ta | in|toa|n | in|tos|i | in|toa|isi (~ in|toisi) | in|non|nee | in|not|koot | in|non|nut | in|not|tiin |
| ir|ro|ta | ir|toa|r | ir|tos|i | ir|toa|isi (~ ir|toisi) | ir|ron|ree | ir|rot|koot | ir|ron|rut | ir|rot|tiir |
| hal|je|ta | hal|kea|n | hal|kes|i | hal|kea|isi (~ hal|keisi) | hal|jen|nee | hal|jet|koot | hal|jen|nut | hal|jet|tiin |
| il|je|tä | il|keä|n | il|kes|i | il|keä|isi (~ il|keisi) | il|jen|nee | il|jet|kööt | il|jen|nyt | il|jet|tiin |
| katketa | katkean (~ katkeen) | katkesi | katke(a)isi | katkennee | katkennut | katkettiin |
| juoruta | juoruta | juoruta | juoru(a)isi | juorunnee | juorunnut | juoruttiin |
| siivota | siivoan (~ siivoon) | siivosi | siivo(a)isi | siivonnee | siivonnut | siivottiin |
| lasso|ta | lasso|a|n | lasso|s|i | lasso|a|isi | lasso|n|nee | lasso|t|koot | lasso|n|nut | lasso|t|tiin |
| myrsky|tä | myrsky|ä|n | myrsky|s|i | myrsky|ä|isi | myrsky|n|nee | myrsky|t|kööt | myrsky|n|nyt | myrsky|t|tiin |
| ryöp|y|tä | ryöp|pyä|n | ryöp|pys|i | ryöp|pyä|isi | ryöp|yn|nee | ryöp|yt|kööt | ryöp|yn|nyt | ryöp|yt|tiin |
| peit|o|ta | peit|toa|n | peit|tos|i | peit|toa|isi | peit|on|nee | peit|ot|koot | peit|on|nut | peit|ot|tiin |
| ker|i|tä | ker|kiä|n | ker|kis|i | ker|kiä|isi | ker|in|nee | ker|it|kööt | ker|in|nyt | ker|it|tiin |
| muo|do|ta | muo|toa|n | muo|tos|i | muo|toa|isi | muo|don|nee | muo|dot|koot | muo|don|nut | muo|dot|tiin |
| läm|mi|tä | läm|piä|n | läm|pis|i | läm|piä|isi | läm|min|nee | läm|mit|kööt | läm|min|nyt | läm|mit|tiin |
| aal|lo|ta | aal|toa|n | aal|tos|i | aal|toa|isi | aal|lon|nee | aal|lot|koot | aal|lon|nut | aal|lot|tiin |
| hel|li|tä | hel|tiä|n | hel|tis|i | hel|tiä|isi | hel|lin|nee | hel|lit|kööt | hel|lin|nyt | hel|lit|tiin |
| selvitä | selviän (~ selviin) | selvisi | selviäisi | selvinnee | selvinnyt | selvittiin |
| tai|ta|a | tai|da|n | tai|s|i | tai|ta|isi | tai|ta|nee ~ tai|n|nee | tai|ta|nut ~ tai|n|nut | tai|det|tiin (~ tai|t|tiin) |
| tie|tä|ä | tie|dä|n | tie|s|i | tie|tä|isi | tie|tä|nee ~ tie|n|nee | tie|tä|nyt ~ tie|n|nyt | tie|det|tiin (~ tie|t|tiin) |
| vipaj|a|a | vipajan| vipaj|i | vipaj|a|isi | vipajanee | vipajanut | vipajettiin|
| heläj|ä|ä | heläjän| heläj|i | heläj|ä|isi | heläjänee | heläjänut | heläjettiin|
| raika|a | raian | raikoi| raika|isi | raikanee | raikanut | raiettiin|

<a href='Hidden comment:  vim: set ft=googlecodewiki:'></a>
