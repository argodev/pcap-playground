from bitstring import BitArray, Bits

class LayerThree(object):

    def __init__(self, bytes=None, little_endian=True):
        """
        Constructor
        Sets the default values for the fields
        """
        if bytes is None:
            self._bits = BitArray()
        else:
            self._bits = BitArray(bytes=bytes)

        self._little_endian = little_endian

    @property
    def data(self):
        return None
    
    def print_details(self):
        print 'Layer three printing'
        print self._bits
