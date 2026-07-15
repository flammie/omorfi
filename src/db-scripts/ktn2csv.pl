#!/usr/bin/perl
#
# (Legacy script which could be rewritten in python and integrated with
#  csv2tsv_guess.py to produce newpara-tsv output without intermediate csv)
#
# Convert following format (field 3 / sample inflections are ignored)
#
#               Mitja    9       Mitja : Mitjan : Mitjaa : ...
#               Jocka    10 -9   Jocka : Jockan : Jockaa : ...
#              Markku    1       Markku : Markun : Markkua : ...
#                Kati    5-AV    Kati : Katin : Katia : ...
#                Ahti    5+-AV   Ahti : Ahdin ... / Ahti : Ahtin ...
#                Yrsa    10/9    Yrsa : Yrsan : Yrsaa : ... Yrsien / Yrsojen
#                 Gay    21i     Gay : Gayn : Gayta : Gayhin : ...
#              Andrew    5/22u   Andrew : Andrewin / Andrew'n : ...
#               Selki    5+AVD   Selki : Selin : ...
#            Ilo|kivi    7       Ilokivi : Ilokiven : Ilokiveä : ...
#                  JP    A0      JP : JP:n : JP:tä ...
#                  DN    A5      DN : DN:n : DN:ää / DN:ä : DN:ään / DN:iin ...
# to -->
#
# "Mitja","9","0","Prop","prop=first"
# "Jocka","10","0","Prop","prop=first"
# "Markku","1","A","Prop","prop=first"
# "Kati","5","0","Prop","prop=first"
# "Ahti","5","F","Prop","prop=first"
# "Ahti","5","0","Prop","prop=first"
# "Yrsa","10","0","Prop","prop=first"
# "Yrsa","9","0","Prop","prop=first"
# "Gay","21","0","Prop","prop=first","stem-vowel=i"
# "Andrew","5","0","Prop","prop=first"
# "Andrew","22","0","Prop","prop=first,"stem-vowel=u"
# "Selki","5","D","Prop","prop=first"
# "Ilokivi","7","0","Prop","prop=first","boundaries=Ilo|kivi"
# "JP","0","0","Acro","prop=first"
# "DN","5","0","Acro","prop=first"
#
# Options:
#  -c "class"      (obligatory) class ~ {N, Prop, A, V, Num}, default: Prop
#  -p "proper-subclass"   (non-oblig.) subclass ~ {first, last, geo, org, misc}
#  -s "semantic subcat"   (non-oblig.) subcat ~ {currency, ..., misc}
#

use utf8;
binmode STDIN, ":encoding(UTF-8)";
binmode STDOUT, ":encoding(UTF-8)";

use Text::Unidecode;
$strip_diacritics = \&unidecode;

use Getopt::Std;
my %opts;
getopt('cps', \%opts);
$class = $opts{'c'} || 'Prop';
$prop_sub = $opts{'p'} || ($class eq 'Prop' ? 'misc' : '');
$sem = $opts{'s'} || '';

sub do_quoted
{
    @r = ();
    for $argm (@_) {
	push @r, '"'.$argm.'"';
    }
    return @r;
}

# Konsonantti
$C = '[kptgbdsfhvjlrmnczwxq]';
# Lyhyt vokaali
$V = '[aeiouyäö]';
# Pitkä vokaali
$VV = '(aa|ee|ii|oo|uu|yy|ää|öö|ai|ei|oi|ui|yi|äi|öi|au|eu|iu|ou|ey|iy|äy|öy|ie|uo|yö)';
# Lyhyt tai pitkä vokaali
$W = "($V|$VV)";

$re_syllable = &$strip_diacritics("$C*($V|$VV)$C*");
$re_two_syllable = '\b(' . $re_syllable . '){2}$';
$re_three_syllable = '\b(' . $re_syllable . '){3}$';

# Return True if given word, or its last compound part, has unambiguously three syllables.
sub three_syllable
{
    my $s = &$strip_diacritics(lc(shift));
    return($s =~ /$re_three_syllable/ and not $s =~ /$re_two_syllable/);
}


# Taivutustyypit, joissa ei astevaihtelua
undef @non_altern;
for (2,3,6,11,12,13,15,17,18,19,20,21,22,29,30,36,37,38,39,40,42,45,46,47,62,63,64,65,68,69,70,71,77)
{ $non_altern[$_] = 1; }     # 44 poistettu Lähdet-tyypin nimiä varten
# Vaihtelevat konsonanttikeskukset
%grading_codes_s = qw/ kk A  pp B  tt C  k D  p E  t F  nk G  mp H  lt I  nt J  rt K 
                      lkk A  lpp B  ltt C  lk D  lp E  nkk A  mpp B  ntt C 
                      rkk A  rpp B  rtt C  rk D  rp E   ht F /;
%grading_codes_w = qw/ k A  p B  t C  ' D  v E  d F  ng G  mm H  ll I  nn J  rr K  lj L  rj L
                      lk A  lp B  lt C  l D  lv E  nk A  mp B  nt C
                      rk A  rp B  rt C  r D  rv E   hj L  hd F /;
$grading_codes_w{''} = 'D';
%grading_centers_s = reverse %grading_codes_s;
%grading_centers_w = reverse %grading_codes_w;

sub find_gra_code
{
    my $word = lc(shift);
    my $num = shift;
    my $plur = shift;
    my ($rev, $cons, $voc, $endcons);

    print STDERR "'$word': missing infl.class number\n" if ! $num;

    return '0' if $non_altern[$num];

    $rev = (($num >= 32 and $num <= 49) or 
	    ($num >= 66 and $num <= 78 and $num != 76));   # käänteinen astevaihtelu
    $rev = !$rev if $plur;

    if ($rev) {
	%grading_codes = %grading_codes_w;
	%grading_centers = %grading_centers_w;
    } else {
	%grading_codes = %grading_codes_s;
	%grading_centers = %grading_centers_s;
    }
    
    if ($num % 1000 < 52) {   # Noun
	if ($plur) {
	    $word =~ s/t$//;
	    $word =~ s/$V$// if !$rev;
	}

	$word =~ /$V($C{0,3})(${V}i?)($C?)$/;
	$cons = $1; $voc = $2; $endcons = $3;

	return '0' if ($endcons and $num < 32);

	return 'D' if $word =~ /((na|u)hka|vihko|pyyh(e|in))$/;  # käytännössä ainoat nominit joissa hk : h
	return 'D' if ($plur and $num > 1000 and $cons eq 'j'); # aika, poika
	return '0' if (!$grading_codes{$cons});

	if (! $plur) {
	    return '0' if $cons =~ /^[kpt]$/ and three_syllable($word);
	    return 'M' if $cons eq 'k' and $word =~ /${C}[uy]k[uy]$/;
	    return '0' if $cons eq '' and $word =~ /$W$C+[uy]e$/;
	    return '0' if $cons =~ /^[rh]j$/ and $word !~ /((lah|poh|rah|veh|per)je)$/;
	    return '0' if $word =~ /${V}in$/ and $word !~ /(^puin|kerroin)$/;
	    return '0' if $word =~ /$V.s$/ and $word !~ /(^oa|^ie|kiua|äe|rui)s$/;
	    return '0' if $cons =~ /^[lr]$/ and $endcons eq 's' and $word !~ /varas$/;
	}
	return '0' if $num == 43 and length($cons) < 2;
	return '0' if $cons =~ /^[lr]$/ and $word =~ /$VV$cons$voc$endcons$/;
	return '0' if $cons =~ /^[lr]?$/ and $word =~ /(^$C?$W$C$C?$W)$cons$voc$endcons$/;
	return '0' if $rev and $cons =~ /^[lr]$/ and $voc =~ /^[ei]/;
	return '0' if $rev and $cons =~ /^[lr]j$/ and $voc =~ /^[^ei]/;
	return 'L' if !$rev and $cons =~ /^[lr]k$/ and $voc =~ /^[ei]/;
	return $grading_codes{$cons};
    } 
    else {    # Verb
	$num = $num % 1000;
	if ($num < 62 or $num == 76) {
	    $word =~ /$V($C{0,3})($V).$/;
	    $cons = $1; $voc = $2;
	}  elsif ($num == 67) {
	    $word =~ /$V($C{0,3})($V)ll.$/;
	    $cons = $1; $voc = $2;
	}  elsif ($num == 66) {
	    $word =~ /$V($C{0,3})($V)ist.$/;
	    $cons = $1; $voc = $2;
	}  elsif ($num >= 72) {
	    $word =~ /$V($C{0,3})($V)t.$/;
	    $cons = $1; $voc = $2;
	}

	return '0' if (!$grading_codes{$cons});
	return '0' if $cons =~ /[kpt]/ and $num == 66;
	return '0' if $cons eq '' and $num == 67 and $word !~ /jaella$/;
	return '0' if $cons =~ /^[lr]$/ and $word =~ /$VV${cons}${voc}t.$/;
	return '0' if $rev and $cons =~ /^[lr]$/ and $voc =~ /^[ei]/;
	return '0' if $rev and $cons =~ /^[lr]j$/ and $voc =~ /^[^ei]/;
	return 'L' if !$rev and $cons =~ /^[lr]k$/ and $voc =~ /^[ei]/;
	return $grading_codes{$cons};
    }
}

#goto test_kotus;

while (<STDIN>) {
    @fields = split /\t/;
    $word = $fields[0];
    $word =~ s/^\s+//;
    @entries = split /\//, (split / -/, $fields[1])[0];
    for $ent (@entries) {
	$ent =~ /^(A?)([0-9]+)([aeiouyäö]?)([+-]+AV[A-M]*)?(\*)?/;
	$acro = $1; $num = $2; $voc = $3; $gra = $4; $plur = $5;

	$wclass = $class;
	$gra_code = '0';
	$bounds = '';

	if ($acro) {            # Acronym w/ possible alternate inflection
	    $wclass = 'Acro';
	}
	elsif ($num == 999) {   # old code for Acronym
	    $wclass = 'Acro';
	    $num = 99;
	}
	elsif ($num == 99) {   # no inflection
	}
	elsif ($gra =~ /^\+\-?AV([A-M])/) {   # pre-defined gradation code
	    $gra_code = $1;
	}
	elsif (!$gra or substr($gra,0,1) eq '+') {
	    $gra_code = find_gra_code($word, $num, $plur);
	}
	if (index($word, '|') > 0) {   # not >= 0: allow lexeme '|'
		$bounds = $word;
		$word =~ tr/|//d;
	}
	@fields = ($word, $num, $gra_code, $wclass);
	@extras = ();
	push @extras, "prop=$prop_sub" if $prop_sub;
	push @extras, "sem=$sem" if $sem;
	push @extras, "stem-vowel=$voc" if $voc;
	push @extras, "plt=obligatory" if $plur;
	push @extras, "boundaries=$bounds" if $bounds;
	push @fields, @extras;
	print join(',', do_quoted(@fields)), "\n";

	if ($gra =~ /^\+\-AV/ and $gra_code ne '0') {
	    @fields[2] = '0';
	    print join(',', do_quoted(@fields)), "\n";
	}
    }
}

exit;


### TESTING with KOTUS.CSV
#
test_kotus:
while (<STDIN>) {
    chomp;
    @fields = split /[,]/;
    for (@fields) {
	$_ =~ s/^\"(.*)\"$/\1/;
    }
    next if $fields[3] !~ /^([V])$/;  # /^([NAV])$/;
    $word = $fields[0];
    $num = $fields[1];
    $correct_code = $fields[2];
    $gra_code = find_gra_code($word, $num);
    if ($gra_code ne $correct_code) {
        print "$num $word - expected code $correct_code, got $gra_code\n";
    }
}
exit; ###

### TESTING with OMORFI_TABLE
#
test_omorfi_table:
while (<STDIN>) {
    chomp;
    @fields = split /\t/;
    next if $fields[0] !~ /^[A-Z]\b/ or $fields[10] =~ /no examples|not possible/;
    $word = $fields[10];
    $word =~ s/XXX//;
    $word =~ s/^\W+//;
    $word =~ s/\W.+//;
    $nss_code = $fields[5];
    $nss_code =~ /^([0-9]+)-?([A-Z]?)/;
    $num = $1; 
    $correct_code = $2 || '0';
    $gra_code = find_gra_code($word, $num);
    if ($gra_code ne $correct_code) {
	print "$num $word - expected code $correct_code, got $gra_code\n";
    }
}
exit; ###
