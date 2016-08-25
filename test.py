
from bitstring import BitArray, Bits
from constants import LinkTypes
from constants import EthernetTypes
from constants import ProtocolNumbers
from PcapGlobalHeader import PcapGlobalHeader
from PcapPacketHeader import PcapPacketHeader
#from EthernetPacket import EthernetPacket
from layers import layertwo
from layers import ethernetframe
from layers import ipv4datagram
from layers import tcpsegment

#test_file = '//c/scratch/equinix-chicago.dirA.20140320-130000.UTC/equinix-chicago.dirA.20140320-130000.UTC.anon.pcap'
test_file = 'c:\scratch\http.pcap'
#test_file = 'c:\scratch\http.pcapng'


# https://wiki.wireshark.org/Development/LibpcapFileFormat
# file "global header"" is as follows:


# http://www.tcpdump.org/linktypes.html


pkt_count = 0
layer_two = None
layer_three = None
layer_four = None


def parse_layer_two(bytes, little_endian):
    if header.network == LinkTypes.LINKTYPE_ETHERNET:
        ethernet = ethernetframe.EthernetFrame(bytes, little_endian)
        ethernet.print_details()
        return ethernet

def parse_layer_three(bytes):
    if header.network == LinkTypes.LINKTYPE_ETHERNET:
        if layer_two.type_length == EthernetTypes.IPV4:
            ipv4 = ipv4datagram.IPv4Datagram(bytes)
            ipv4.print_details()
            return ipv4

def parse_layer_four(bytes):
    if header.network == LinkTypes.LINKTYPE_ETHERNET:
        if layer_two.type_length == EthernetTypes.IPV4:
            if layer_three.protocol == ProtocolNumbers.TCP:
                tcp = tcpsegment.TcpSegment(bytes)
                tcp.print_details()
                return tcp

# open the file for reading (r) in binary (b) mode
with open(test_file, "rb") as f:

    # attempt to read the global header
    header_bytes = f.read(24)
    header = PcapGlobalHeader(header_bytes)
    header.print_details()
    
    # attempt to read a packet
    packet_header_bytes = f.read(16)

    while packet_header_bytes != "":
        pkt_count += 1
        packet_header = PcapPacketHeader(packet_header_bytes, header.little_endian)
        print "=============================="
        packet_header.print_details()

        # read and drop the packet data bytes
        packet_data_bytes = f.read(packet_header.incl_len)

        layer_two = parse_layer_two(packet_data_bytes, header.little_endian)
        layer_three = parse_layer_three(layer_two.data)
        layer_four = parse_layer_four(layer_three.data)

        # get the header for the next packet
        packet_header_bytes = f.read(16)
        break


print "Total Packets: " + str(pkt_count)