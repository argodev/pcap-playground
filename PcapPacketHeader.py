from bitstring import BitArray, Bits

class PcapPacketHeader(object):
    """
    typedef struct pcaprec_hdr_s {
            (4) guint32 ts_sec;         /* timestamp seconds */
            (4) guint32 ts_usec;        /* timestamp microseconds */
            (4) guint32 incl_len;       /* number of octets of packet saved in file */
            (4) guint32 orig_len;       /* actual length of packet */
    } pcaprec_hdr_t;
    """
    def __init__(self, bytes=None, little_endian=True):
        """
        Constructor
        Sets the default values for the fields
        """
        # packet is 16 bytes long
        if bytes is None:
            self._bits = BitArray(length=128)
        else:
            self._bits = BitArray(bytes=bytes)

        self._little_endian = little_endian

    @property
    def ts_sec(self):
        if self._little_endian:
            return self._bits[0:32].uintle
        else:
            return self._bits[0:32].uintbe

    @property
    def ts_usec(self):
        if self._little_endian:
            return self._bits[32:64].uintle
        else:
            return self._bits[32:64].uintbe

    @property
    def incl_len(self):
        if self._little_endian:
            return self._bits[64:96].uintle
        else:
            return self._bits[64:96].uintbe

    @property
    def orig_len(self):
        if self._little_endian:
            return self._bits[96:128].uintle
        else:
            return self._bits[96:128].uintbe
    
    def print_details(self):
        print "Timestamp Seconds: " + str(self.ts_sec)
        print "Timestamp microSeconds: " + str(self.ts_usec)
        print "Included Bytes: " + str(self.incl_len)
        print "Original Bytes: " + str(self.orig_len)
