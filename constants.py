
class Protocol_Numbers(object):
    HOPOPT = 0
    ICMP = 1
    IGMP = 2
    GGP = 3
    IPV4 = 4
    ST = 5
    TCP = 6
    CBT = 7

    @staticmethod
    name_from_value(value):
        if value == HOPOPT:
            return 'HOPOPT'
        elif value == ICMP:
            return 'ICMP'
        elif value == IGMP:
            return 'IGMP'
        elif value == GGP:
            return 'GGP'
        elif value == IPV4:
            return 'IPv4'
        elif value == ST:
            return 'ST'
        elif value == TCP:
            return 'TCP'
        elif value == CBT:
            return 'CBT'
        else:
            return str(value)