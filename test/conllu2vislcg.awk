function ufeat2vislish(udstring)
{
    if (udstring == "_")
    {
        return "";
    }
    split(udstring, feats, /\|/);
    rv = "";
    for (n in feats)
    {
        split(feats[n], kv, /=/);
        if ((kv[1] == "Number") && (kv[2] == "Sing")) { rv = rv " SG"; }
        else if ((kv[1] == "Number") && (kv[2] == "Plur")) { rv = rv " PL"; }
        else if ((kv[1] == "Person")) { rv = rv " PERS+" kv[2]; }
        else if ((kv[1] == "Person")) { rv = rv " PERS+" kv[2]; }
        else if ((kv[1] == "Person['psor']")) { rv = rv " POSS+" kv[2]; }
        else if ((kv[1] == "Person['psor']")) { rv = rv " POSS+" kv[2]; }
        else if ((kv[1] == "Number['psor']") && (kv[2] == "Sing")) { rv = rv " POSSPL"; }
        else if ((kv[1] == "Number['psor']") && (kv[2] == "Plur")) { rv = rv " POSSPL"; }
        else if (kv[2] == "Pres") { rv = rv " PRESENT"; }
        else if ((kv[1] == "PartForm") && (kv[2] == "Past")) { rv = rv " PCPNUT"; }
        else if ((kv[1] == "PartForm") && (kv[2] == "Pres")) { rv = rv " PCPVA"; }
        else if (kv[2] == "Past") { rv = rv " PAST"; }
        else if ((kv[1] == "PronType") && (kv[2] == "Ind")) { rv = rv; }
        else if (kv[2] == "Ind") { rv = rv " INDV"; }
        else if (kv[2] == "Cnd") { rv = rv " COND"; }
        else if (kv[2] == "Imp") { rv = rv " IMPV"; }
        else if (kv[2] == "Pass") { rv = rv " PSS"; }
        else if (kv[1] == "Connegative") { rv = rv " CONNEG"; }
        else if ((kv[1] == "InfForm") && (kv[2] == "1")) { rv = rv " INFA"; }
        else if ((kv[1] == "InfForm") && (kv[2] == "2")) { rv = rv " INFE"; }
        else if ((kv[1] == "InfForm") && (kv[2] == "3")) { rv = rv " INFMA"; }
        else if ((kv[1] == "VerbForm")) { rv = rv; }
        else if ((kv[1] == "Derivation")) { rv = rv " <" kv[2] ">"; }
        else { rv = rv " " toupper(kv[2]); }
    }
    gsub(/PL PERS\+/, "PL", rv);
    gsub(/SG PERS\+/, "SG", rv);
    return rv;
}
/^$/ {print;}
/^#/ {print;}
$1 ~ /[0-9]+/  {printf("\"<%s>\"\n\t\"%s\" %s%s\n", $2, $3, $4,
    ufeat2vislish($6));}

