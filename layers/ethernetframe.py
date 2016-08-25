from bitstring import BitArray, Bits
from constants import EthernetTypes
from layertwo import LayerTwo

class EthernetFrame(LayerTwo):

    # @property
    # def preamble(self):
    #     if self._little_endian:
    #         return self._bits[0:64].uintle
    #     else:
    #         return self._bits[0:64].uintbe

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

    @property
    def data(self):
        # start at 112, go to length - 32
        data_start = 112
        data_end = self._bits.length - 32
        return self._bits[data_start:data_end].tobytes()
    
    @property
    def crc(self):
        return self._bits.length/8
        #pass


    def print_details(self):
        #print "Preamble: " + str(self.preamble)
        print "Destination MAC: " + EthernetFrame.format_mac_address(self.destination_mac_address)
        print "Source MAC:      " + EthernetFrame.format_mac_address(self.source_mac_address)
        print "Type/Length:     " + hex(self.type_length) + " (" + str(EthernetTypes.name_from_value(self.type_length)) + ")"
        print "CRC Checksum:    " + str(self.crc)

    @staticmethod
    def format_mac_address(address):
        return ':'.join(a+b for a,b in zip(address[::2], address[1::2]))

    def get_layer_three_bytes(self):
        # figure out what we have used, and pass on the rest
        pass

        
