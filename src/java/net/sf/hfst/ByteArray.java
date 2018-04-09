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

    /** Create byte array from int.
     *
     * @param s  int to convert
     */
    public ByteArray(int s)
    {
	size = s;
	bytes = new byte[size];
	index = 0;
    }

    /** Create byte array from byte array.
     *
     * @param another  array to convert
     * @param s  size to convert
     */
    public ByteArray(ByteArray another, int s)
    {
	size = Math.max(s, another.getSize());
	bytes = new byte[size];
	for (int i = 0; i < another.getSize(); ++i) {
	    bytes[i] = another.get(i);
	}
	index = 0;
    }

    /** Get byte array size.
     *
     * @return  the size*/
    public int getSize()
    {
	return size;
    }

    /** Get a byte.
     *
     * @param i  index of byte.
     * @return  byte at the index
     */
    public byte get(int i)
    {
	return bytes[i];
    }

    /** Get all bytes.
     *
     * @return all bytes
     */
    public byte[] getBytes()
    {
	return bytes;
    }

    /** Get unsigned byte.
     *
     * @return  unsigned byte
     */
    public short getUByte()
    {
	short result = 0;
	result |= bytes[index];
	index += 1;
	return result;
    }

    /** Get unsigned short.
     *
     * @return  unsigned short
     */
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

    /** Get unsigned int.
     *
     * @return unsigned int
     */
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

    /** Get unsigned bool.
     *
     * @return  unsigned bool
     */
    public Boolean getBool() throws java.io.IOException
    {
	if (this.getUInt() == 0)
	    { return false; }
	return true;
    }

    /** Get unsigned float.
     *
     * @return  unsigned float
     */
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
