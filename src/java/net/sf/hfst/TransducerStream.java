package net.sf.hfst;

import java.io.DataInputStream;

/**
 * A simple extension of DataInputStream to handle unsigned
 * little-endian data.
 */
public class TransducerStream extends DataInputStream
{
    /**
     * Invokes the DataInputStream constructor with a BufferedInputStream
     * argument.
     * @param stream BufferedInputStream containing little-endian unsigned variables
     */
    public TransducerStream(DataInputStream stream)
    { super(stream); }

    /**
     * Reads the next two bytes as an unsigned little-endian short.
     * @return an int representing the unsigned short
     */
    public int getUShort() throws java.io.IOException
    {
	short byte1 = (short) this.readUnsignedByte();
	short byte2 = (short) this.readUnsignedByte();
	int result = 0;
	result |= byte2;
	result <<= 8;
	result |= byte1;
	return result;
    }

    /**
     * Reads the next four bytes as an unsigned little-endian int.
     * @return a long representing the unsigned int
     */
    public long getUInt() throws java.io.IOException
    {
	short byte1 = (short) this.readUnsignedByte();
	short byte2 = (short) this.readUnsignedByte();
	short byte3 = (short) this.readUnsignedByte();
	short byte4 = (short) this.readUnsignedByte();
	long result = 0;
	result |= byte4;
	result <<= 8;
	result |= byte3;
	result <<= 8;
	result |= byte2;
	result <<= 8;
	result |= byte1;
	return result;
    }

    /**
     * Reads four bytes (sic), returns false if they're all zero
     * and true otherwise.
     * @return a boolean representing the underlying unsigned int
     */
    public Boolean getBool() throws java.io.IOException
    {
	if (this.getUInt() == 0)
	    { return false; }
	return true;
    }
}
