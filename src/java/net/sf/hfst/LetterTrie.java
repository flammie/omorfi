package net.sf.hfst;

import java.util.Hashtable;

/**
 * A suffix tree of letters.
 */
public class LetterTrie
{
    /** A node in a letter trie. */
    public class LetterTrieNode
    {
	private Hashtable<Character, Integer> symbols;
	private Hashtable<Character, LetterTrieNode> children;

    /** add a string to trie.
     *
     * @param str  a token to add as letter
     * @param symbolNumber  number for the token
     */
	public void addString(String str, Integer symbolNumber)
	{
	    if (str.length() > 1)
		{
		    if (children.containsKey(str.charAt(0)) == false)
			{
			    children.put(str.charAt(0), new LetterTrieNode());
			}
		    children.get(str.charAt(0))
			.addString(str.substring(1,str.length()),
				   symbolNumber);
		} else if (str.length() == 1)
		{
		    symbols.put(str.charAt(0), symbolNumber);
		}
	}

    /** Get index of the string.
     *
     * @param string  string to find
     * @return  index number
     */
	public int findKey(IndexString string)
	{
	    if (string.index >= string.str.length())
		{
		    return HfstOptimizedLookup.NO_SYMBOL_NUMBER;
		}
	    Character at_s = string.str.charAt(string.index);
	    ++string.index;
	    if (children.containsKey(at_s) == false)
		{
		    if (symbols.get(at_s) == null)
			{
			    --string.index;
			    return HfstOptimizedLookup.NO_SYMBOL_NUMBER;
			}
		    return symbols.get(at_s);
		}
	    int s = children.get(at_s).findKey(string);
	    if (s == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{
		    if (symbols.get(at_s) == null)
			{
			    --string.index;
			    return HfstOptimizedLookup.NO_SYMBOL_NUMBER;
			}
		    return symbols.get(at_s);
		}
	    return s;
	}

    /** Create a node for letter trie. */
	public LetterTrieNode()
	{
	    symbols = new Hashtable<Character, Integer>();
	    children = new Hashtable<Character, LetterTrieNode>();
	}
    }

    private LetterTrieNode root;

    /** Create a letter trie. */
    public LetterTrie()
    {
	root = new LetterTrieNode();
    }

    /** Add string to letters of the trie.
     *
     * @param str  string to ad ass a letter.
     * @param symbolNumber  number for the index
     */
    public void addString(String str, Integer symbolNumber)
    {
	root.addString(str, symbolNumber);
    }

    /** Find index of the string.
     *
     * @param str  string to look for.
     */
    Integer findKey(IndexString str)
    {
	return root.findKey(str);
    }
}

