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
        rv = rv " " feats[n];
    }
    return rv;
}
/^$/ {print;}
/^#/ {print;}
$1 ~ /[0-9]+/  {printf("\"<%s>\"\n\t\"%s\" UPOS=%s%s\n", $2, $3, $4,
    ufeat2vislish($6));}

