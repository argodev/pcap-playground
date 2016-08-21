from bitstring import BitArray, Bits
from link_types import LinkTypes

class IPv4Header(object):
    def __init__(self, bytes=None):
        """
        Constructor
        Sets the default values for the fields
        """
        
        if bytes is None:
            self._bits = BitArray(length=192)
        else:
            self._bits = BitArray(bytes=bytes)

    @property
    def version(self):
        return self._bits[0:4].uintle

    @property
    def ihl(self):
        return self._bits[4:8].uintle

    @property
    def dscp(self):
        return self._bits[8:14].uintle

    @property
    def ecn(self):
        return self._bits[14:16].uintle

    @property
    def total_length(self):
        return self._bits[16:32].uintle

    @property
    def identification(self):
        return self._bits[32:48].uintle

    @property
    def flags(self):
        return self._bits[48:51]

    @property
    def fragment_offset(self):
        return self._bits[51:64].uintle

    @property
    def time_to_live(self):
        return self._bits[64:72].uintle

    @property
    def protocol(self):
        return self._bits[72:80].uintle

    @property
    def header_checksum(self):
        return self._bits[80:96].uintle

    @property
    def source_ip(self):
        return self._bits[96:128].uintle

    @property
    def destination_ip(self):
        return self._bits[128:160].uintle


        
