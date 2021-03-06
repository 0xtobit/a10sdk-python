from a10sdk.common.A10BaseClass import A10BaseClass


class Netflow(A10BaseClass):
    
    """Class Description::
    Configure NetFlow/IPFIX.

    Class netflow supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param monitor_list: {"minItems": 1, "items": {"type": "monitor"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"source-ip-use-mgmt": {"default": 0, "optional": true, "type": "number", "description": "Use management interface's IP address for source ip of netflow packets", "format": "flag"}, "protocol": {"description": "'v9': Netflow version 9; 'v10': Netflow version 10 (IPFIX); ", "format": "enum", "default": "v9", "type": "string", "enum": ["v9", "v10"], "optional": true}, "name": {"description": "Name of netflow monitor", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "source-address": {"type": "object", "properties": {"ip": {"type": "string", "description": "Specify source IP address", "format": "ipv4-address"}, "ipv6": {"type": "string", "description": "Specify source IPv6 address", "format": "ipv6-address"}}}, "destination": {"type": "object", "properties": {"ip-cfg": {"type": "object", "properties": {"ip": {"not-list": ["service-group", "ipv6"], "type": "string", "description": "IP address of netflow collector", "format": "ipv4-address"}, "port4": {"description": "Port number, default is 9996", "format": "number", "default": 9996, "maximum": 65535, "minimum": 1, "type": "number"}}}, "service-group": {"description": "Service-group for load balancing between multiple collector servers", "format": "string-rlx", "minLength": 1, "not-list": ["ip", "ipv6"], "maxLength": 63, "type": "string"}, "ipv6-cfg": {"type": "object", "properties": {"port6": {"description": "Port number, default is 9996", "format": "number", "default": 9996, "maximum": 65535, "minimum": 1, "type": "number"}, "ipv6": {"not-list": ["service-group", "ip"], "type": "string", "description": "IPv6 address of netflow collector", "format": "ipv6-address"}}}}}, "sample": {"type": "object", "properties": {"ve-list": {"minItems": 1, "items": {"type": "ve"}, "uniqueItems": true, "array": [{"required": ["ve-num"], "properties": {"ve-num": {"description": "VE interface number", "format": "number", "optional": false, "maximum": 4094, "minimum": 2, "type": "number", "$ref": "/axapi/v3/interface/ve"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/ve/{ve-num}"}, "nat-pool-list": {"minItems": 1, "items": {"type": "nat-pool"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"pool-name": {"description": "Name of nat pool", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/nat-pool/{pool-name}"}, "ethernet-list": {"minItems": 1, "items": {"type": "ethernet"}, "uniqueItems": true, "array": [{"required": ["ifindex"], "properties": {"ifindex": {"optional": false, "$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet interface number", "format": "interface"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}/sample/ethernet/{ifindex}"}}}, "record": {"type": "object", "properties": {"sesn-event-nat64": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}, "nat64": {"default": 0, "type": "number", "description": "NAT64 Flow Record Template", "format": "flag"}, "dslite": {"default": 0, "type": "number", "description": "DS-Lite Flow Record Template", "format": "flag"}, "nat44": {"default": 0, "type": "number", "description": "NAT44 Flow Record Template", "format": "flag"}, "netflow-v5-ext": {"default": 0, "type": "number", "description": "Extended NetFlow V5 Flow Record Template, supports ipv6", "format": "flag"}, "port-mapping-nat64": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}, "sesn-event-dslite": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}, "sesn-event-nat44": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}, "netflow-v5": {"default": 0, "type": "number", "description": "NetFlow V5 Flow Record Template", "format": "flag"}, "port-mapping-dslite": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}, "port-mapping-nat44": {"enum": ["both", "creation", "deletion"], "type": "string", "description": "'both': Export both creation and deletion events; 'creation': Export only creation events; 'deletion': Export only deletion events; ", "format": "enum"}}}, "disable": {"default": 0, "optional": true, "type": "number", "description": "Disable this netflow monitor", "format": "flag"}, "resend-template": {"type": "object", "properties": {"records": {"description": "To resend template once for each number of records (Number of records: default is 1000, 0 means never resend template)", "format": "number", "default": 1000, "maximum": 1000000, "minimum": 0, "type": "number"}, "timeout": {"description": "To set time interval to resend template (number of seconds: default is 1800, 0 means never resend template)", "format": "number", "default": 1800, "maximum": 86400, "minimum": 0, "type": "number"}}}, "flow-timeout": {"description": "Configure timeout value to export flow records periodically for long-live session ( Number of minutes: default is 10, 0 means only send flow record when session is deleted)", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 0, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/netflow/monitor/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "netflow"
        self.a10_url="/axapi/v3/netflow"
        self.DeviceProxy = ""
        self.monitor_list = []
        self.common = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


