from a10sdk.common.A10BaseClass import A10BaseClass


class Inbound(A10BaseClass):
    
    """Class Description::
    Stateless NAT46 fragmentation rules for inbound oversize packets.

    Class inbound supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'drop': Drop Silently; 'ipv4': Use IPv4 fragmentation for oversize packets (default); 'send-icmpv6': Send ICMP Type 2 Code 0 (Packet Too Big); ", "format": "enum", "default": "ipv4", "type": "string", "enum": ["drop", "ipv4", "send-icmpv6"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless/fragmentation/inbound`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "inbound"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless/fragmentation/inbound"
        self.DeviceProxy = ""
        self.action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


