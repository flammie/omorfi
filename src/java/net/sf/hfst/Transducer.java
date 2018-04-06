package net.sf.hfst;

import java.util.Collection;

public abstract class Transducer {
    public abstract Collection<String> analyze(String str) throws NoTokenizationException;
}
