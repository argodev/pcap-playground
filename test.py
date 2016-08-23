
from bitstring import BitArray, Bits
from link_types import LinkTypes
from PcapGlobalHeader import PcapGlobalHeader
from PcapPacketHeader import PcapPacketHeader
from EthernetPacket import EthernetPacket

#test_file = '//c/scratch/equinix-chicago.dirA.20140320-130000.UTC/equinix-chicago.dirA.20140320-130000.UTC.anon.pcap'
test_file = 'c:\scratch\http.pcap'
#test_file = 'c:\scratch\http.pcapng'


# https://wiki.wireshark.org/Development/LibpcapFileFormat
# file "global header"" is as follows:


# http://www.tcpdump.org/linktypes.html


pkt_count = 0

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

        if header.network == LinkTypes.LINKTYPE_ETHERNET:
            packet = EthernetPacket(packet_data_bytes, header.little_endian)
            packet.print_details()
            packet.process_layer_three()

        # get the header for the next packet
        packet_header_bytes = f.read(16)
        #break


print "Total Packets: " + str(pkt_count)