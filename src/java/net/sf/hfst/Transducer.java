package net.sf.hfst;

import java.util.Collection;

/** A simple interface to a transducer */
public abstract class Transducer {
    /** Analyse a string and get all possible readings.
     *
     * @param str  token to analyse
     * @return  all possible analyses of the token
     */
    public abstract Collection<String> analyze(String str) throws NoTokenizationException;
}
