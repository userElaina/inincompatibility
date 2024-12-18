import time
from lib1 import time_out, _inincompatibility_client_connect_callback
from lib1 import _inincompatibility_client_close_callback
from inincompatibility import IServer

if __name__ == '__main__':
    inincs = IServer(
        addr=('localhost', 23333),
        listen_n=4,
        multi='multiprocessing',
        verbose=True
    )
    inincs.client_connect_callback = _inincompatibility_client_connect_callback
    inincs.client_close_callback = _inincompatibility_client_close_callback
    inincs.add_funcs(time_out)
    inincs.gen_import_code()
    inincs.start()
    inincs.run()
