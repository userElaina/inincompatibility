from lib1 import getdata, calc, _inincompatibility_client_connect_callback
from lib1 import _inincompatibility_client_close_callback
from inincompatibility import IServer

inincs = IServer(verbose=True)
inincs.client_connect_callback = _inincompatibility_client_connect_callback
inincs.client_close_callback = _inincompatibility_client_close_callback
inincs.add_funcs(getdata, calc)
inincs.run()
