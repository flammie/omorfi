package net.sf.hfst;

import java.lang.Math; // heh

/**
 * A way of handling unsigned little-endian data
 */
public class ByteArray
{
    private byte[] bytes;
    private int index;
    private int size;

    public ByteArray(int s)
    {
	size = s;
	bytes = new byte[size];
	index = 0;
    }
    
    public ByteArray(ByteArray another, int s)
    {
	size = Math.max(s, another.getSize());
	bytes = new byte[size];
	for (int i = 0; i < another.getSize(); ++i) {
	    bytes[i] = another.get(i);
	}
	index = 0;
    }

    public int getSize()
    {
	return size;
    }

    public byte get(int i)
    {
	return bytes[i];
    }

    public byte[] getBytes()
    {
	return bytes;
    }

    public short getUByte()
    {
	short result = 0;
	result |= bytes[index];
	index += 1;
	return result;
    }

    public int getUShort() throws java.io.IOException
    {
	int result = 0;
	result |= (bytes[index+1] & 0xFF);
	// even java's bytes are always signed - isn't that convenient?
	result <<= 8;
	result |= (bytes[index] & 0xFF);
	index += 2;
	return result;
    }

    public long getUInt() throws java.io.IOException
    {
	long result = 0;
	result |= (bytes[index+3] & 0xFF);
	result <<= 8;
	result |= (bytes[index+2] & 0xFF);
	result <<= 8;
	result |= (bytes[index+1] & 0xFF);
	result <<= 8;
	result |= (bytes[index] & 0xFF);
	index += 4;
	return result;
    }

    public Boolean getBool() throws java.io.IOException
    {
	if (this.getUInt() == 0)
	    { return false; }
	return true;
    }

    public float getFloat() throws java.io.IOException
    {
	int bits = 0;
	bits |= (bytes[index+3] & 0xFF);
	bits <<= 8;
	bits |= (bytes[index+2] & 0xFF);
	bits <<= 8;
	bits |= (bytes[index+1] & 0xFF);
	bits <<= 8;
	bits |= (bytes[index] & 0xFF);
	index += 4;
	return Float.intBitsToFloat(bits);
    }
}