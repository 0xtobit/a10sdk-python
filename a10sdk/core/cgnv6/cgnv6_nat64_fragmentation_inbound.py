from a10sdk.common.A10BaseClass import A10BaseClass


class Inbound(A10BaseClass):
    
    """Class Description::
    Fragmentation Behavior from NAT outside to NAT inside.

    Class inbound supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param count: {"description": "Configure number of ICMP messages sent when DF set. Default is 1", "format": "number", "default": 1, "optional": true, "maximum": 5, "minimum": 1, "type": "number"}
    :param frag_action: {"description": "'drop': Drop Silently; 'ipv6': Use IPv6 fragmentation for oversize packets (default); ", "format": "enum", "default": "ipv6", "type": "string", "enum": ["drop", "ipv6"], "optional": true}
    :param df_set: {"description": "'drop': Drop Silently; 'ipv6': Use IPv6 fragmentation; 'send-icmp': Send ICMP Type 3 Code 4 (Fragmentation Needed and DF Set) (default); ", "format": "enum", "default": "send-icmp", "type": "string", "enum": ["drop", "ipv6", "send-icmp"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/fragmentation/inbound`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "inbound"
        self.a10_url="/axapi/v3/cgnv6/nat64/fragmentation/inbound"
        self.DeviceProxy = ""
        self.count = ""
        self.frag_action = ""
        self.df_set = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


