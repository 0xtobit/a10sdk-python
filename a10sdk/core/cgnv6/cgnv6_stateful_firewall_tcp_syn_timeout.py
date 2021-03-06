from a10sdk.common.A10BaseClass import A10BaseClass


class SynTimeout(A10BaseClass):
    
    """Class Description::
    Configure TCP SYNtimeout.

    Class syn-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param syn_timeout_val: {"description": "Set Seconds session can remain in half-open state before being deleted (default: 4 seconds)", "format": "number", "default": 4, "optional": true, "maximum": 30, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/tcp/syn-timeout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "syn-timeout"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/tcp/syn-timeout"
        self.DeviceProxy = ""
        self.syn_timeout_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


