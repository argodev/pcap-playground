from bitstring import BitArray, Bits
from link_types import LinkTypes

class PcapGlobalHeader(object):
    """
    typedef struct pcap_hdr_s {
        (4) guint32 magic_number;   /* magic number */
        (2) guint16 version_major;  /* major version number */
        (2) guint16 version_minor;  /* minor version number */
        (4) gint32  thiszone;       /* GMT to local correction */
        (4) guint32 sigfigs;        /* accuracy of timestamps */
        (4) guint32 snaplen;        /* max length of captured packets, in octets */
        (4) guint32 network;        /* data link type */
    } pcap_hdr_t;
    """
    def __init__(self, bytes=None):
        """
        Constructor
        Sets the default values for the fields
        """
        # packet is 24 bytes long
        if bytes is None:
            self._bits = BitArray(length=192)
        else:
            self._bits = BitArray(bytes=bytes)

    @property
    def magic_number(self):
        """magic number
        """
        return self._bits[0:32].hex

    @property
    def valid_pcap_file(self):
        return (self._bits[0:32] == Bits('0xd4c3b2a1')) or \
                (self._bits[0:32] == Bits(' 0xa1b2c3d4'))
    @property
    def little_endian(self):
        return self._bits[0:32] ==  Bits('0xd4c3b2a1')

    @property
    def version_major(self):
        if self.little_endian:
            return self._bits[32:48].uintle
        else:
            return self._bits[32:48].uintbe

    @property
    def version_minor(self):
        if self.little_endian:
            return self._bits[48:64].uintle
        else:
            return self._bits[48:64].uintbe

    @property
    def this_zone(self):
        if self.little_endian:
            return self._bits[64:96].intle
        else:
            return self._bits[64:96].intbe

    @property
    def sig_figs(self):
        if self.little_endian:
            return self._bits[96:128].uintle
        else:
            return self._bits[96:128].uintbe

    @property
    def snap_len(self):
        if self.little_endian:
            return self._bits[128:160].uintle
        else:
            return self._bits[128:160].uintbe

    @property
    def network(self):
        if self.little_endian:
            return self._bits[160:192].uintle
        else:
            return self._bits[160:192].uintbe

    def print_details(self):
        print "Magic Number: " + str(self.magic_number)
        print "Valid PCAP File: " + str(self.valid_pcap_file)
        print "File Version: " + str(self.version_major) + "." + str(self.version_minor)
        print "Timezone Offset: " + str(self.this_zone)
        print "Timestamp Accuracy: " + str(self.sig_figs)
        print "Snap Length: " + str(self.snap_len)
        print "Data Link Type: " + LinkTypes.translate_to_string(self.network)

