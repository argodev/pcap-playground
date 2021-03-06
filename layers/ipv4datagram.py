from bitstring import BitArray, Bits
from constants import ProtocolNumbers
from layerthree import LayerThree

# http://www.tutorialspoint.com/ipv4/ipv4_packet_structure.htm
class IPv4Datagram(LayerThree):

    @property
    def version(self):
        return self._bits[0:4].uint

    @property
    def ihl(self):
        """Internet Header Length
        
        The number of 32-bit words in the header
        """
        return self._bits[4:8].uint

    @property
    def dscp(self):
        """Differentiated Services Field
        """
        return self._bits[8:14].uint

    @property
    def ecn(self):
        """Explicit Congestion Notification
        """
        return self._bits[14:16].uint

    @property
    def total_length(self):
        return self._bits[16:32].uint

    @property
    def identification(self):
        return self._bits[32:48].uint

    @property
    def flags(self):
        return self._bits[48:51]

    @property
    def fragment_offset(self):
        return self._bits[51:64].uint

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
    def source_ip_string(self):
        return '{}.{}.{}.{}'.format(
            self._bits[96:104].uintle,
            self._bits[104:112].uintle,
            self._bits[112:120].uintle,
            self._bits[120:128].uintle
        )

    @property
    def destination_ip(self):
        return self._bits[128:160].uintle

    @property
    def destination_ip_string(self):
        return '{}.{}.{}.{}'.format(
            self._bits[128:136].uintle,
            self._bits[136:144].uintle,
            self._bits[144:152].uintle,
            self._bits[152:160].uintle
        )

    @property
    def options(self):
        if self.ihl > 5:
            pass
        else:
            return None

    @property
    def data(self):
        # start at 112, go to length - 32
        data_start = self.ihl * 32
        data_end = self._bits.length
        return self._bits[data_start:data_end].tobytes()


    def print_details(self):
        print "\t********************************"
        print "\t IPv4"
        print "\t Version:         " + str(self.version)
        print "\t Header Length:   " + str(self.ihl)
        print "\t DSCP:            " + str(self.dscp)
        print "\t ECN:             " + str(self.ecn)
        print "\t Total Length:    " + str(self.total_length)
        print "\t Identification:  " + str(self.identification)
        print "\t Flags:           " + str(self.flags)
        print "\t Fragment Offset: " + str(self.fragment_offset)
        print "\t Time To Live:    " + str(self.time_to_live)
        print "\t Protocol:        " + ProtocolNumbers.name_from_value(self.protocol) + " (" + str(self.protocol) + ")"
        print "\t Header Checksum: " + str(self.header_checksum)
        print "\t Source IP:       " + str(self.source_ip) + " (" + self.source_ip_string + ")"
        print "\t Destination IP:  " + str(self.destination_ip) + " (" + self.destination_ip_string + ")"


        
