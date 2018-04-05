package net.sf.hfst;

import java.io.DataInputStream;
import java.util.Vector;
import java.util.Hashtable;

/**
 * On instantiation reads the transducer's alphabet and provides an interface
 * to it. Flag diacritic parsing is also handled here.
 */
public class TransducerAlphabet
{
    public Vector<String> keyTable;
    public Hashtable<Integer, FlagDiacriticOperation> operations;
    public Integer features;
    public TransducerAlphabet(DataInputStream charstream,
		    int number_of_symbols) throws java.io.IOException
    {
	keyTable = new Vector<String>();
	operations = new Hashtable<Integer, FlagDiacriticOperation>();
	Hashtable<String, Integer> feature_bucket = new Hashtable<String, Integer>();
	Hashtable<String, Integer> value_bucket = new Hashtable<String, Integer>();
	features = 0;
	Integer values = 1;
	value_bucket.put("", 0); // neutral value
	int i = 0;
	int charindex;
	byte[] chars = new byte[1000]; // FIXME magic number
	while (i < number_of_symbols)
	    {
		charindex = 0;
		chars[charindex] = charstream.readByte();
		while (chars[charindex] != 0)
		    {
			++charindex;
			chars[charindex] = charstream.readByte();
		    }
		String ustring = new String(chars, 0, charindex, "UTF-8");
		if (ustring.length() > 5 && ustring.charAt(0) == '@' && ustring.charAt(ustring.length()-1) == '@' && ustring.charAt(2) == '.')
		    { // flag diacritic identified
			HfstOptimizedLookup.FlagDiacriticOperator op;
			String[] parts = ustring.substring(1,ustring.length()-1).split("\\.");
			/* Not a flag diacritic after all, ignore it */
			if (parts.length < 2) {
			    keyTable.add("");
			    i++;
			    continue;
			}
			String ops = parts[0];
			String feats = parts[1];
			String vals;
			if (parts.length == 3) {
			    vals = parts[2];
			} else {
			    vals = "";
			}
			if (ops.equals("P")) {
			    op = HfstOptimizedLookup.FlagDiacriticOperator.P;
			} else if (ops.equals("N")) {
			    op = HfstOptimizedLookup.FlagDiacriticOperator.N;
			} else if (ops.equals("R")) {
				op = HfstOptimizedLookup.FlagDiacriticOperator.R;
			} else if (ops.equals("D")) {
			    op = HfstOptimizedLookup.FlagDiacriticOperator.D;
			} else if (ops.equals("C")) {
			    op = HfstOptimizedLookup.FlagDiacriticOperator.C;
			} else if (ops.equals("U")) {
			    op = HfstOptimizedLookup.FlagDiacriticOperator.U;
			} else { // Not a valid operator, ignore the operation
			    keyTable.add("");
			    i++;
			    continue;
			}
			if (value_bucket.containsKey(vals) == false) {
				value_bucket.put(vals, values);
				values++;
			    }
			if (feature_bucket.containsKey(feats) == false) {
			    feature_bucket.put(feats, features);
			    features++;
			}
			operations.put(i, new FlagDiacriticOperation(op,
								     feature_bucket.get(feats),
								     value_bucket.get(vals)));
			keyTable.add("");
			i++;
			continue;
		    }
		keyTable.add(ustring);
		i++;
	    }
	keyTable.set(0, ""); // epsilon is zero
    }
}
