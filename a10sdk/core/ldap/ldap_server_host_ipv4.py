from a10sdk.common.A10BaseClass import A10BaseClass


class PortCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ssl: {"default": 0, "type": "number", "description": "Use SSL", "format": "flag"}
    :param port: {"description": "Specify the LDAP server's port (default 389 without ssl or 636 with ssl)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param timeout: {"description": "Specify the LDAP server's timeout (default 3)", "minimum": 1, "type": "number", "maximum": 60, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-cfg"
        self.DeviceProxy = ""
        self.ssl = ""
        self.port = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4(A10BaseClass):
    
    """Class Description::
    Specify the hostname of ldap server.

    Class ipv4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4_addr: {"optional": false, "type": "string", "description": "IPV4 address of ldap server", "format": "ipv4-address"}
    :param cn_value: {"description": "LDAP common name identifier (i.e.: cn, uid)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param dn_value: {"description": "LDAP distinguished name (dn)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ldap-server/host/ipv4/{ipv4_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4_addr"]

        self.b_key = "ipv4"
        self.a10_url="/axapi/v3/ldap-server/host/ipv4/{ipv4_addr}"
        self.DeviceProxy = ""
        self.port_cfg = {}
        self.ipv4_addr = ""
        self.cn_value = ""
        self.dn_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


