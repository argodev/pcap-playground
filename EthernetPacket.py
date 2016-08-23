from bitstring import BitArray, Bits
from link_types import LinkTypes
import EthernetTypes
from IPv4Header import IPv4Header


class EthernetPacket(object):
    def __init__(self, bytes=None, little_endian=True):
        """
        Constructor
        Sets the default values for the fields
        """
        # defaults to 64 bytes long
        if bytes is None:
            self._bits = BitArray(length=512)
        else:
            self._bits = BitArray(bytes=bytes)

        self._little_endian = little_endian

    @property
    def preamble(self):
        if self._little_endian:
            return self._bits[0:64].uintle
        else:
            return self._bits[0:64].uintbe

    @property
    def destination_mac_address(self):
        if self._little_endian:
            return self._bits[0:48].hex
        else:
            return self._bits[0:48].hex

    @property
    def source_mac_address(self):
        if self._little_endian:
            return self._bits[48:96].hex
        else:
            return self._bits[48:96].hex

    @property
    def type_length(self):
        if self._little_endian:
            return int(self._bits[96:112].hex, 16)
        else: 
            return self._bits[96:112].intbe

    def print_details(self):
        print "Preamble: " + str(self.preamble)
        print "Destination MAC: " + EthernetPacket.format_mac_address(self.destination_mac_address)
        print "Source MAC:      " + EthernetPacket.format_mac_address(self.source_mac_address)
        print "Type/Length:     " + hex(self.type_length) + " (" + str(EthernetPacket.translate_type(self.type_length)) + ")"

    @staticmethod
    def format_mac_address(address):
        return ':'.join(a+b for a,b in zip(address[::2], address[1::2]))

    @staticmethod
    def translate_type(hex_type):
        if hex_type == EthernetTypes.IPV4: return 'IPv4'
        if hex_type == EthernetTypes.ARP: return 'ARP'
        if hex_type == EthernetTypes.IPV6: return 'IPv6'

    def process_layer_three(self):
        if self.type_length == EthernetTypes.IPV4:
            ipv4 = IPv4Header(self._bits[112:272].tobytes())
            ipv4.print_details()
            pass
        elif self.type_length == EthernetTypes.IPV6:
            pass
        elif self.type_length == EthernetTypes.ARP:
            pass
        
