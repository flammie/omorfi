package net.sf.hfst;

import java.io.DataInputStream;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

import net.sf.hfst.Transducer;
import net.sf.hfst.NoTokenizationException;

/**
 * Reads the header, alphabet, index table and transition table and provides
 * interfaces to them.
 */
public class WeightedTransducer extends Transducer
{

    /** a weighted transion index. */
    public class TransitionIndex
    {
        /** input symbol */
	protected int inputSymbol;
    /** first transition index */
	protected long firstTransitionIndex;

    /** create index
     *
     * @param input input symbol
     * @param firstTransition index
     */
	public TransitionIndex(int input, long firstTransition)
	    {
        /** input symbol */
		inputSymbol = input;
    /** index for first transition */
		firstTransitionIndex = firstTransition;
	    }

    /** whether index matches  symbol
     * @param s index
     * @return true if matches, false otherwise
     */
	public Boolean matches(int s)
	{
	    if (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return false; }
	    if (s == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return true; }
	    return (s == inputSymbol);
	}

    /** whether is final
     * @return true if final. false otherwise
     */
	public Boolean isFinal()
	{
	    return (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    firstTransitionIndex != HfstOptimizedLookup.NO_TABLE_INDEX);
	}

    /** gets final weight.
     *
     * @return weight
     */
	public float getFinalWeight()
	{ return Float.intBitsToFloat((int)firstTransitionIndex); }


    /** gets target
     * @return index of target
     */
	    public long target()
	{ return firstTransitionIndex; }


        /** gets input symbol
         * @return input symbol key
         */
	public int getInput()
	{ return inputSymbol; }
    }



    /**
     * On instantiation reads the transducer's index table and provides an interface
     * to it.
     */
    public class IndexTable
    {
	private TransitionIndex[] indices;

    /** Read index from transducer data.
     *
     * @param filestream  transducer data stream at index position
     * @param indicesCount  size of index
     */
	public IndexTable(FileInputStream filestream,
			  Integer indicesCount) throws java.io.IOException
	{
	    ByteArray b = new ByteArray((int) indicesCount*6);
	    filestream.read(b.getBytes());
	    // each index entry is a unsigned short followed by an unsigned int
	    indices = new TransitionIndex[indicesCount];

	    Integer i = 0;
	    while (i < indicesCount)
		{
		    indices[i] = new TransitionIndex(b.getUShort(), b.getUInt());
		    i++;
		}
	}

    /** Whether state at index is final.
     * @param index index of the state
     * @return true if final, else otherwise.
     */
	public Boolean isFinal(Integer index)
	{ return indices[index].isFinal(); }

    /** Get index at position.
     * @param index index of the state
     * @return index to transitions.
     */
    public TransitionIndex at(Integer index)
	{ return indices[index]; }

    }

    /** A weighted transition. */
    public class Transition
    {
        /** input symbol */
	protected int inputSymbol;
    /** output symbol */
	protected int outputSymbol;
    /** target index */
	protected long targetIndex;
    /** weight */
	protected float weight;

    /** Create a weighted transition
     *
     * @param input  input symbol
     * @param output  output symbol
     * @param target  target state index
     * @param w  weight
     */
	public Transition(int input, int output, long target, float w)
	{
	    inputSymbol = input;
	    outputSymbol = output;
	    targetIndex = target;
	    weight = w;
	}

    /** Create default transition. */
	public Transition()
	{
	    inputSymbol = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	    outputSymbol = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	    targetIndex = Long.MAX_VALUE;
	    weight = HfstOptimizedLookup.INFINITE_WEIGHT;
	}

    /** Whether transition matches the symbol.
     *
     * @param symbol symbol key
     * @return true if transition is for symbol, false otherwise
     */
	public Boolean matches(int symbol)
	{
	    if (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return false; }
	    if (symbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return true; }
	    return (inputSymbol == symbol);
	}
    /** Get target state.
     * @return target state index.
     */
	public long target()
	{ return targetIndex; }

    /** Get output symbol.
     * @return output symbol
     */
	public int getOutput()
	{ return outputSymbol; }

    /** Get input symbol
     * @return input symbol
     */
	public int getInput()
	{ return inputSymbol; }

    /**
     * Whether the state is final.
     * @return  true if final, false otherweise.
     */
	public Boolean isFinal()
	{
	    return (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    outputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    targetIndex == 1);
	}

    /** get weight.
     * @return weight
     */
	public float getWeight()
	{ return weight; }
    }

    /**
     * On instantiation reads the transducer's transition table and provides an
     * interface to it.
     */
    public class TransitionTable
    {
	private Transition[] transitions;

    /** Read transitions from transducer file data.
     *
     * @param filestream input data pointing at the transitions
     * @param transitionCount  number of transitions to read.
     */
	public TransitionTable(FileInputStream filestream,
			       Integer transitionCount) throws java.io.IOException
	{
	    ByteArray b = new ByteArray((int) transitionCount*12);
	    // 12 bytes per transition
	    // each transition entry is two unsigned shorts, an unsigned int and a float
	    filestream.read(b.getBytes());
	    transitions = new Transition[transitionCount];
	    Integer i = 0;
	    while (i < transitionCount)
		{
		    transitions[i] = new Transition(b.getUShort(), b.getUShort(), b.getUInt(), b.getFloat());
		    i++;
		}
	}

    /** get transition at index.
     * @param pos  index
     * @return a transition
     */
	public Transition at(Integer pos)
	{ return transitions[pos]; }


    /** get size of index.
     * @return size
     */
	public Integer size()
	{ return transitions.length; }

    }

    /** header */
    protected TransducerHeader header;
    /** alphabet */
    protected TransducerAlphabet alphabet;
    /** states */
    protected Stack<int[]> stateStack;
    /** flag operations */
    protected Hashtable<Integer, FlagDiacriticOperation> operations;
    /** letters */
    protected LetterTrie letterTrie;
    /** indices */
    protected IndexTable indexTable;
    /** transitions */
    protected TransitionTable transitionTable;
    /** display vector */
    protected Vector<String> displayVector;
    /** output string */
    protected int[] outputString;
    /** input string */
    protected Vector<Integer> inputString;
    /** output pointer */
    protected int outputPointer;
    /** input pointer */
    protected int inputPointer;
    /** weight */
    protected float current_weight;

    /** Read a transducer from data.
     *
     * @param file  data  stream pointing to transudcer binary
     * @param h  header read from the stream
     * @param a alphabet read from the stream
     */
    public WeightedTransducer(FileInputStream file, TransducerHeader h, TransducerAlphabet a) throws java.io.IOException
    {
	header = h;
	alphabet = a;
	stateStack = new Stack< int[] >();
	int[] neutral = new int[alphabet.features];
	for (int i = 0; i < neutral.length; ++i) {
	    neutral[i] = 0;
	}
	stateStack.push(neutral);
	operations = alphabet.operations;
	letterTrie = new LetterTrie();
	int i = 0;
	while (i < header.getInputSymbolCount())
	    {
		letterTrie.addString(alphabet.keyTable.get(i), i);
		i++;
	    }
	indexTable = new IndexTable(file, header.getIndexTableSize());
	transitionTable = new TransitionTable(file, header.getTargetTableSize());
	displayVector = new Vector<String>();
	outputString = new int[1000];
	for (i = 0; i < 1000; i++)
	    { outputString[i] = HfstOptimizedLookup.NO_SYMBOL_NUMBER; }
	inputString = new Vector<Integer>();
	outputPointer = 0;
	inputPointer = 0;
	current_weight = 0.0f;
    }

    private int pivot(long i)
    {
	if (i >= HfstOptimizedLookup.TRANSITION_TARGET_TABLE_START) {
	    return (int) (i - HfstOptimizedLookup.TRANSITION_TARGET_TABLE_START);
	}
	return (int) i;
    }

    private void tryEpsilonIndices(int index)
    {
	if (indexTable.at(index).getInput() == 0)
	    {
		tryEpsilonTransitions(pivot(indexTable.at(index).target()));
	    }
    }

    private void tryEpsilonTransitions(int index)
    {
	while (true)
	    {
		// first test for flag
		if (operations.containsKey(transitionTable.at(index).getInput())) {
		    if (!pushState(operations.get(transitionTable.at(index).getInput())))
			{
			    ++index;
			    continue;
			} else {
			outputString[outputPointer] = transitionTable.at(index).getOutput();
			++outputPointer;
			current_weight += transitionTable.at(index).getWeight();
			getAnalyses(transitionTable.at(index).target());
			current_weight -= transitionTable.at(index).getWeight();
			--outputPointer;
			++index;
			stateStack.pop();
			continue;
		    }
		} else if (transitionTable.at(index).getInput() == 0)
		    { // epsilon transitions
			outputString[outputPointer] = transitionTable.at(index).getOutput();
			++outputPointer;
			current_weight += transitionTable.at(index).getWeight();
			getAnalyses(transitionTable.at(index).target());
			current_weight -= transitionTable.at(index).getWeight();
			--outputPointer;
			++index;
			continue;
		    }
		else
		    {
			break;
		    }
	    }
    }

    private void findIndex(int index)
    {
	if (indexTable.at(index + (inputString.get(inputPointer - 1))).getInput() == inputString.get(inputPointer - 1))
	    {
		findTransitions(pivot(indexTable.at(index + inputString.get(inputPointer - 1)).target()));
	    }
    }

    private void findTransitions(int index)
    {
	while (transitionTable.at(index).getInput() != HfstOptimizedLookup.NO_SYMBOL_NUMBER)
	    {
		if (transitionTable.at(index).getInput() == inputString.get(inputPointer - 1))
		    {
			outputString[outputPointer] = transitionTable.at(index).getOutput();
			++outputPointer;
			current_weight += transitionTable.at(index).getWeight();
			getAnalyses(transitionTable.at(index).target());
			current_weight -= transitionTable.at(index).getWeight();
			--outputPointer;
		    } else
		    {
			return;
		    }
		++index;
	    }
    }

    private void getAnalyses(long idx)
    {
	if (idx >= HfstOptimizedLookup.TRANSITION_TARGET_TABLE_START)
	    {
		int index = pivot(idx);
		tryEpsilonTransitions(pivot(index) + 1);
		if (inputString.get(inputPointer) == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		    { // end of input string
			outputString[outputPointer] = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
			if (transitionTable.size() <= index)
			    { return; }
			if (transitionTable.at(index).isFinal())
			    {
				current_weight += transitionTable.at(index).getWeight();
				noteAnalysis();
				current_weight -= transitionTable.at(index).getWeight();
			    }
			return;
		    }
		++inputPointer;
		findTransitions(index + 1);
	    } else
	    {
		int index = pivot(idx);
		tryEpsilonIndices(index + 1);
		if (inputString.get(inputPointer) == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		    { // end of input string
			outputString[outputPointer] = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
			if (indexTable.isFinal(index))
			    {
				current_weight += indexTable.at(index).getFinalWeight();
				noteAnalysis();
				current_weight -= indexTable.at(index).getFinalWeight();
			    }
			return;
		    }
		++inputPointer;
		findIndex(index + 1);
	    }
	--inputPointer;
	outputString[outputPointer] = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
    }

    private void noteAnalysis()
    {
	int i = 0;
	displayVector.add("");
	while (outputString[i] != HfstOptimizedLookup.NO_SYMBOL_NUMBER)
	    {
		displayVector.set(displayVector.size() - 1, displayVector.lastElement() + alphabet.keyTable.get(outputString[i]));
		++i;
	    }
	displayVector.set(displayVector.size() - 1, displayVector.lastElement() + "\t" + current_weight);
    }

    /** Analyse a string.
     *
     * @param input  a token to analyse
     * @return  all possible analyses for input
     */
    public Collection<String> analyze(String input)
	throws NoTokenizationException
    {
	inputString.clear();
	displayVector.clear();
	outputPointer = 0;
	outputString[0] = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	inputPointer = 0;

	IndexString inputLine = new IndexString(input);
	while (inputLine.index < input.length())
	    {
		inputString.add(letterTrie.findKey(inputLine));
		if (inputString.lastElement() == HfstOptimizedLookup.NO_SYMBOL_NUMBER) {
		    break;
		}
	    }
	if ( (inputString.size() == 0) || (inputString.lastElement() == HfstOptimizedLookup.NO_SYMBOL_NUMBER) )
	    {
		throw new NoTokenizationException(input);
	    }
	inputString.add(HfstOptimizedLookup.NO_SYMBOL_NUMBER);
	getAnalyses(0);
	return new ArrayList<String>(displayVector);
    }

        private Boolean pushState(FlagDiacriticOperation flag)
    {
	int[] top = new int[alphabet.features];
	System.arraycopy(stateStack.peek(), 0, top, 0, alphabet.features);
	if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.P) { // positive set
	    stateStack.push(top);
	    stateStack.peek()[flag.feature] = flag.value;
	    return true;
	} else if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.N) { // negative set
	    stateStack.push(top);
	    stateStack.peek()[flag.feature] = -1*flag.value;
	    return true;
	} else if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.R) { // require
	    if (flag.value == 0) // empty require
		{
		    if (stateStack.peek()[flag.feature] == 0)
			{
			    return false;
			}
		    else
			{
			    stateStack.push(top);
			    return true;
			}
		}
	    else {
		if (stateStack.peek()[flag.feature] == flag.value) {
		    stateStack.push(top);
		    return true;
		}
	    }
	    return false;
	} else if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.D) { // disallow
	    if (flag.value == 0) // empty disallow
		{
		    if (stateStack.peek()[flag.feature] != 0)
			{
			    return false;
			}
		    else
			{
			    stateStack.push(top);
			    return true;
			}
		}
	    else {
		if (stateStack.peek()[flag.feature] == flag.value) {
			return false;
		}
	    }
	    stateStack.push(top);
	    return true;
	} else if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.C) { // clear
	    stateStack.push(top);
	    stateStack.peek()[flag.feature] = 0;
	    return true;
	} else if (flag.op == HfstOptimizedLookup.FlagDiacriticOperator.U) { // unification
	    if ((stateStack.peek()[flag.feature] == 0) ||
		(stateStack.peek()[flag.feature] == flag.value) ||
		(stateStack.peek()[flag.feature] != flag.value &&
		 stateStack.peek()[flag.feature] < 0)) {

		    stateStack.push(top);
		    stateStack.peek()[flag.feature] = flag.value;
		    return true;
		}
	    return false;
	}
	return false; // compiler sanity
    }
}
