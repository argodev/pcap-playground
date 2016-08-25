from bitstring import BitArray, Bits

class TcpHeader(object):
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
        return self._bits[0:4].uint

    def print_details(self):
        print "\t********************************"
        print "\t IPv4"
        print "\t Version:         " + str(self.version)
        print "\t Internet Header Length: " + str(self.ihl)
        print "\t DSCP:            " + str(self.dscp)
