package net.sf.hfst;

/**
 * A representation of one flag diacritic statement
 */
public class FlagDiacriticOperation
{
    /** Operation type. */
    public HfstOptimizedLookup.FlagDiacriticOperator op;
    /** Feature number. */
    public Integer feature;
    /** Feature value. */
    public Integer value;


    /** Create a flag diacritic operation.
     *
     * @param operation  operation of the flag
     * @param feat  feature name
     * @param val   feature value
     */
    public FlagDiacriticOperation(HfstOptimizedLookup.FlagDiacriticOperator operation,
				  Integer feat, Integer val)
    {
	op = operation;
	feature = feat;
	value = val;
    }

    /** Create a flag diacritic operation. */
    public FlagDiacriticOperation()
    {
	op = HfstOptimizedLookup.FlagDiacriticOperator.P;
	feature = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	value = 0;
    }

    /** Whether flag diacritic operation is a flag.
     *
     * @return  true this is a flag and known, false otherwise
     */
    public Boolean isFlag()
    {
	return feature != HfstOptimizedLookup.NO_SYMBOL_NUMBER;
    }
}
