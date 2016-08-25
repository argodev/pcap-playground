
# here we define the ethernet types we recognize
IPV4 = 0x0800
ARP  = 0x0806
IPV6 = 0x86dd

def name_from_value(value):
    if value == IPV4:
        return 'IPv4'
    elif value == ARP:
        return 'ARP'
    elif value == IPV6:
        return 'IPv6'
    else:
        return str(value)