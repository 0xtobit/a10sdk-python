from a10sdk.common.A10BaseClass import A10BaseClass


class HostList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_host: {"minLength": 1, "maxLength": 31, "type": "string", "description": "DNS remote host", "format": "string"}
    :param ipv4_mask: {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "host-list"
        self.DeviceProxy = ""
        self.dns_host = ""
        self.ipv4_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_host: {"type": "string", "description": "IPV4 remote host", "format": "ipv4-address"}
    :param ipv4_mask: {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv4-list"
        self.DeviceProxy = ""
        self.ipv4_host = ""
        self.ipv4_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_host: {"type": "string", "description": "IPV6 remote host", "format": "ipv6-address"}
    :param ipv6_mask: {"description": "IPV6 mask", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-list"
        self.DeviceProxy = ""
        self.ipv6_host = ""
        self.ipv6_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Remote(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param host_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-host": {"minLength": 1, "maxLength": 31, "type": "string", "description": "DNS remote host", "format": "string"}, "optional": true, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}
    :param ipv4_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ipv4-host": {"type": "string", "description": "IPV4 remote host", "format": "ipv4-address"}, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}
    :param ipv6_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-host": {"type": "string", "description": "IPV6 remote host", "format": "ipv6-address"}, "optional": true, "ipv6-mask": {"description": "IPV6 mask", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "remote"
        self.DeviceProxy = ""
        self.host_list = []
        self.ipv4_list = []
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Read(A10BaseClass):
    
    """Class Description::
    Define a read only community string.

    Class read supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param user: {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param oid_list: {"minItems": 1, "items": {"type": "oid"}, "uniqueItems": true, "array": [{"required": ["oid-val"], "properties": {"remote": {"type": "object", "properties": {"host-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-host": {"minLength": 1, "maxLength": 31, "type": "string", "description": "DNS remote host", "format": "string"}, "optional": true, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv4-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ipv4-host": {"type": "string", "description": "IPV4 remote host", "format": "ipv4-address"}, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv6-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-host": {"type": "string", "description": "IPV6 remote host", "format": "ipv6-address"}, "optional": true, "ipv6-mask": {"description": "IPV6 mask", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}}}]}}}, "oid-val": {"description": "specific the oid (The oid value, object-key)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/community/read/{user}/oid/{oid-val}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/community/read/{user}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "user"]

        self.b_key = "read"
        self.a10_url="/axapi/v3/snmp-server/community/read/{user}"
        self.DeviceProxy = ""
        self.remote = {}
        self.user = ""
        self.oid_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


