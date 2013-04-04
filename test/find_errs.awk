NF > 2 { none = 1 
        for (i = 3; i <= NF; i++) {
                if ($2 == $i) { rests += 1; none = 0; break; }
        }
        incorrects += none;
        if (none == 1) {
            print;
        }
    }
NF > 1 { lines += 1; }
