package net.sf.hfst;

//import java.io.DataInputStream;
import java.io.FileInputStream;
import net.sf.hfst.FormatException;

/**
 * On instantiation reads the transducer's header and provides an interface
 * to it.
 */
public class TransducerHeader
{
    private int number_of_input_symbols;
    private int number_of_symbols;
    private int size_of_transition_index_table;
    private int size_of_transition_target_table;
    private int number_of_states;
    private int number_of_transitions;

    private Boolean weighted;
    private Boolean deterministic;
    private Boolean input_deterministic;
    private Boolean minimized;
    private Boolean cyclic;
    private Boolean has_epsilon_epsilon_transitions;
    private Boolean has_input_epsilon_transitions;
    private Boolean has_input_epsilon_cycles;
    private Boolean has_unweighted_input_epsilon_cycles;

    private Boolean hfst3;
    private Boolean intact;

    /**
     * Read in the (56 bytes of) header information, which unfortunately
     * is mostly in little-endian unsigned form.
     *
     * @param file file stream pointing to a header
     */
    public TransducerHeader(FileInputStream file) throws java.io.IOException, FormatException
    {
	hfst3 = false;
	intact = true; // could add some checks to toggle this and check outside
	ByteArray head = new ByteArray(5);
	file.read(head.getBytes());
	if (begins_hfst3_header(head)) {
	    read_hfst3_header(file);
	    file.read(head.getBytes());
	    hfst3 = true;
	}
	ByteArray b = new ByteArray(head, 56);
	file.read(b.getBytes(), 5, 51);

	number_of_input_symbols = b.getUShort();
	number_of_symbols = b.getUShort();
	size_of_transition_index_table = (int) b.getUInt();
	size_of_transition_target_table = (int) b.getUInt();
	number_of_states = (int) b.getUInt();
	number_of_transitions = (int) b.getUInt();

	weighted = b.getBool();
	deterministic = b.getBool();
	input_deterministic = b.getBool();
	minimized = b.getBool();
	cyclic = b.getBool();
	has_epsilon_epsilon_transitions = b.getBool();
	has_input_epsilon_transitions = b.getBool();
	has_input_epsilon_cycles = b.getBool();
	has_unweighted_input_epsilon_cycles = b.getBool();
    }

    /** whether bytes start with HFST 3 header
     *
     * @param bytes bytes to check
     * @return true if HFST3 header, false otherwise
     */
    public Boolean begins_hfst3_header(ByteArray bytes)
    {
	if (bytes.getSize() < 5) {
	    return false;
	}
	// HFST\0
	return (bytes.getUByte() == 72 && bytes.getUByte() == 70 &&
		bytes.getUByte() == 83 && bytes.getUByte() == 84 &&
		bytes.getUByte() == 0);
    }

    /** read HFST 3 header.
     * @param file file that contains a header
     */
    public void read_hfst3_header(FileInputStream file) throws java.io.IOException, FormatException
    {
        // The only thing we really check is that the format begins with
        // HFST_OL. First we read the two bytes giving the header size...
	ByteArray len = new ByteArray(2);
	file.read(len.getBytes());
        // Then we read the rest...
        ByteArray header = new ByteArray(len.getUShort() + 1);
        file.read(header.getBytes());
        // And just convert it to a String and see if the type is set to what we want
        String s = new String(header.getBytes(), "UTF-8");
        if (s.indexOf("type\0HFST_OL") == -1) {
            throw new FormatException();
        }

    }
    /** Get input symbol count
     * @return input symbol count
     */
    public int getInputSymbolCount()
    { return number_of_input_symbols; }

    /** Get symbol count
     * @return  symbol count
     */
    public int getSymbolCount()
    { return number_of_symbols; }

    /** Get index table size
     * @return index table size
     */
    public int getIndexTableSize()
    { return size_of_transition_index_table; }

    /** Get target table size
     * @return target table size
     */
    public int getTargetTableSize()
    { return size_of_transition_target_table; }

    /** Whether it's weighted.
     * @return true if weighted, false otherwise
     */
    public Boolean isWeighted()
    { return weighted; }

    /** Whether it's hfst 3 header.
     * @return true if header, false otherwise
     */
    public Boolean hasHfst3Header()
    { return hfst3; }

    /** Whether it's intact.
     * @return true if intact, false otherwise
     */
    public Boolean isIntact()
    { return intact; }
}
