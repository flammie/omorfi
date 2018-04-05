package net.sf.hfst;

/**
 * A representation of one flag diacritic statement
 */
public class FlagDiacriticOperation
{
    public HfstOptimizedLookup.FlagDiacriticOperator op;
    public Integer feature;
    public Integer value;
    public FlagDiacriticOperation(HfstOptimizedLookup.FlagDiacriticOperator operation,
				  Integer feat, Integer val)
    {
	op = operation;
	feature = feat;
	value = val;
    }

    public FlagDiacriticOperation()
    {
	op = HfstOptimizedLookup.FlagDiacriticOperator.P;
	feature = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	value = 0;
    }

    public Boolean isFlag()
    {
	return feature != HfstOptimizedLookup.NO_SYMBOL_NUMBER;
    }
}
