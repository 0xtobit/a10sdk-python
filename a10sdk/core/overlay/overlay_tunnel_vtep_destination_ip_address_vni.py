from a10sdk.common.A10BaseClass import A10BaseClass


class Vni(A10BaseClass):
    
    """Class Description::
    Virtual Segment Id configured on the remote VTEP.

    Class vni supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param segment: {"description": "VNI configured for the remote VTEP", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip_address}/vni/{segment}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "segment"]

        self.b_key = "vni"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip_address}/vni/{segment}"
        self.DeviceProxy = ""
        self.segment = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


