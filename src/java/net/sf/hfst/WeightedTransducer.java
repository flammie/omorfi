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

    public class TransitionIndex
    {
	protected int inputSymbol;
	protected long firstTransitionIndex;
	
	public TransitionIndex(int input, long firstTransition)
	    {
		inputSymbol = input;
		firstTransitionIndex = firstTransition;
	    }
	
	public Boolean matches(int s)
	{
	    if (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return false; }
	    if (s == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return true; }
	    return (s == inputSymbol);
	}
	
	public Boolean isFinal()
	{
	    return (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    firstTransitionIndex != HfstOptimizedLookup.NO_TABLE_INDEX);
	}

	public float getFinalWeight()
	{ return Float.intBitsToFloat((int)firstTransitionIndex); }
	
	    public long target()
	{ return firstTransitionIndex; }
	
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

	public Boolean isFinal(Integer index)
	{ return indices[index].isFinal(); }

	public TransitionIndex at(Integer index)
	{ return indices[index]; }

    }
    
    public class Transition
    {
	protected int inputSymbol;
	protected int outputSymbol;
	protected long targetIndex;
	protected float weight;
	
	public Transition(int input, int output, long target, float w)
	{
	    inputSymbol = input;
	    outputSymbol = output;
	    targetIndex = target;
	    weight = w;
	}

	public Transition()
	{
	    inputSymbol = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	    outputSymbol = HfstOptimizedLookup.NO_SYMBOL_NUMBER;
	    targetIndex = Long.MAX_VALUE;
	    weight = HfstOptimizedLookup.INFINITE_WEIGHT;
	}
	
	public Boolean matches(int symbol)
	{
	    if (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return false; }
	    if (symbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER)
		{ return true; }
	    return (inputSymbol == symbol);
	}
	public long target()
	{ return targetIndex; }
	
	public int getOutput()
	{ return outputSymbol; }
	
	public int getInput()
	{ return inputSymbol; }
	
	public Boolean isFinal()
	{
	    return (inputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    outputSymbol == HfstOptimizedLookup.NO_SYMBOL_NUMBER &&
		    targetIndex == 1);
	}

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

	public Transition at(Integer pos)
	{ return transitions[pos]; }

	public Integer size()
	{ return transitions.length; }

    }

    protected TransducerHeader header;
    protected TransducerAlphabet alphabet;
    protected Stack<int[]> stateStack;
    protected Hashtable<Integer, FlagDiacriticOperation> operations;
    protected LetterTrie letterTrie;
    protected IndexTable indexTable;
    protected TransitionTable transitionTable;
    protected Vector<String> displayVector;
    protected int[] outputString;
    protected Vector<Integer> inputString;
    protected int outputPointer;
    protected int inputPointer;
    protected float current_weight;
    
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
