BEGIN { firsts = 0; seconds = 0; thirds = 0; fourths = 0; fifths = 0;
        rests = 0; lines = 0; unresulteds = 0; incorrects = 0; }
NF == 2 { unresulteds += 1; }
NF > 2 { none = 1 
        if ($2 == $3) { firsts += 1; none = 0; }
         else if ($2 == $4) { seconds += 1; none = 0; }
         else if ($2 == $5) { thirds += 1; none = 0; }
         else if ($2 == $6) { fourths += 1; none = 0; }
         else if ($2 == $7) { fifths += 1; none = 0; }
         else
            for (i = 8; i <= NF; i++) {
                if ($2 == $i) { rests += 1; none = 0; break; }
            }
        incorrects += none;
    }
NF > 1 { lines += 1; }
END {
    printf("Firsts\t1-5\tAny\n");
    printf("%.2f %%\t%.2f %%\t %.2f %%\n", firsts/lines * 100,
        (firsts + seconds + thirds + fourths + fifths) / lines * 100,
        (firsts + seconds + thirds + fourths + fifths + rests) / lines * 100);
}
