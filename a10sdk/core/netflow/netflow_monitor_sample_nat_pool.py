from a10sdk.common.A10BaseClass import A10BaseClass


class NatPool(A10BaseClass):
    
    """Class Description::
    Select nat pool to monitor.

    Class nat-pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_name: {"description": "Name of nat pool", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/monitor/{name}/sample/nat-pool/{pool_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "nat-pool"
        self.a10_url="/axapi/v3/netflow/monitor/{name}/sample/nat-pool/{pool_name}"
        self.DeviceProxy = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


