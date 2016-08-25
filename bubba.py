from bitstring import BitArray, Bits
from layers.layertwo import LayerTwo

class b1(object):
    def __init__(self, bytes=None, little_endian=True):
        if bytes is None:
            self._bits = BitArray()
        else:
            self._bits = BitArray(bytes=bytes)

        self._little_endian = little_endian

    def print_details(self):
        print 'Layer two printing'
        print self._bits

class b2(b1):
    def my_type(self):
        print 'my type'

    @property
    def my_name(self):
        print 'my name'

class b3(LayerTwo):

    @property
    def type_length(self):
        print 'slick'



x = LayerTwo()
x = b3()
print dir(x)
x.print_details()
x.type_length

