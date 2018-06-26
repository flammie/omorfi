package net.sf.hfst;

/** An exception for tokenisation errors. */
public class NoTokenizationException extends Exception {
    /** The string sought for. */
    String attempted;
    /** Create an exception for given untokenisable string.
     *
     * @param str  string that couldn't be tokenised.
     */
    public NoTokenizationException(String str)
	{
	    super();
	    attempted = str;
	}

    /** Fromat exception as human readable stirng.
     *
     * @return a human readable message for error
     */
    public String message()
    {
	return "Failed to tokenize " + attempted;
    }
}
