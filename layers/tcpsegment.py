from bitstring import BitArray, Bits
from constants import ProtocolNumbers
from layerfour import LayerFour

# http://www.tutorialspoint.com/ipv4/ipv4_packet_structure.htm
class TcpSegment(LayerFour):
    pass

    @property
    def source_port(self):
        return self._bits[0:16].uint

    @property
    def destination_port(self):
        return self._bits[16:32].uint

    @property
    def sequence_number(self):
        return self._bits[32:64].uint

    @property
    def acknowledgement_number(self):
        return self._bits[64:96].uint

    @property
    def data_offset(self):
        """ 32-bit words
        """
        return self._bits[96:100].uint

    @property
    def data_offset_bytes(self):
        return self.data_offset * 4

    @property
    def reserved(self):
        return self._bits[100:103].uint

    @property
    def ns(self):
        return self._bits[103:104].bool

    @property
    def cwr(self):
        return self._bits[104:105].bool

    @property
    def ece(self):
        return self._bits[105:106].bool

    @property
    def urg(self):
        return self._bits[106:107].bool

    @property
    def ack(self):
        return self._bits[107:108].bool

    @property
    def psh(self):
        return self._bits[108:109].bool

    @property
    def rst(self):
        return self._bits[109:110].bool

    @property
    def syn(self):
        return self._bits[110:111].bool

    @property
    def fin(self):
        return self._bits[111:112].bool

    @property
    def window_size(self):
        return self._bits[112:128].uint

    @property
    def checksum(self):
        return self._bits[128:144].hex

    @property
    def urgent_pointer(self):
        return self._bits[144:160].uint

    @property
    def options_length(self):
        return (self.data_offset - 5) * 4

    @property
    def data(self):
        data_start = self.data_offset * 32
        data_end = self._bits.length
        return self._bits[data_start:data_end].tobytes()


    def print_details(self):
        print '\t'
        print "\t Source Port:      " + str(self.source_port)
        print "\t Destination Port: " + str(self.destination_port)
        print "\t Sequence Number:  " + str(self.sequence_number)
        print "\t Acknowledgement Number:  " + str(self.acknowledgement_number)
        print "\t Data Offset:      " + str(self.data_offset)
        print "\t Data Offset (Bytes): " + str(self.data_offset_bytes)
        print "\t Reserved:            " + str(self.reserved)
        print "\t NS:            " + str(self.ns)
        print "\t CWR:            " + str(self.cwr)
        print "\t ECE:            " + str(self.ece)
        print "\t URG:            " + str(self.urg)
        print "\t ACK:            " + str(self.ack)
        print "\t PSH:            " + str(self.psh)
        print "\t RST:            " + str(self.rst)
        print "\t SYN:            " + str(self.syn)
        print "\t FIN:            " + str(self.fin)
        print "\t Window Size:    " + str(self.window_size)
        print "\t Checksum:       " + str(self.checksum)
        print "\t Urgent Pointer: " + str(self.urgent_pointer)
        print "\t Options Length: " + str(self.options_length)

    #     print "\t ECN:             " + str(self.ecn)
    #     print "\t Total Length:    " + str(self.total_length)
    #     print "\t Identification:  " + str(self.identification)
    #     print "\t Flags:           " + str(self.flags)
    #     print "\t Fragment Offset: " + str(self.fragment_offset)
    #     print "\t Time To Live:    " + str(self.time_to_live)
    #     print "\t Protocol:        " + ProtocolNumbers.name_from_value(self.protocol) + " (" + str(self.protocol) + ")"
    #     print "\t Header Checksum: " + str(self.header_checksum)
    #     print "\t Source IP:       " + str(self.source_ip) + " (" + self.source_ip_string + ")"
    #     print "\t Destination IP:  " + str(self.destination_ip) + " (" + self.destination_ip_string + ")"