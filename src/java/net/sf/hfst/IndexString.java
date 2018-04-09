package net.sf.hfst;

// There has to be a better way...
/** A tuple of string and index. */
public class IndexString
{
    /** String member */
    public String str;
    /** Index member */
    public int index;
    /** Create and index string.
     *
     * @param s  string member
     */
    public IndexString(String s)
    {
	str = s;
	index = 0;
    }
}

