from a10sdk.common.A10BaseClass import A10BaseClass


class HttpBasic(A10BaseClass):
    
    """Class Description::
    HTTP Basic Authentication Relay.

    Class http-basic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"name": {"description": "Specify HTTP basic authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/http-basic/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/http-basic`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http-basic"
        self.a10_url="/axapi/v3/aam/authentication/relay/http-basic"
        self.DeviceProxy = ""
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


