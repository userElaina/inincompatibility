import sys
assert sys.version_info.minor >= 11
import time


def _inincompatibility_client_connect_callback(addr) -> int:
    print('_inincompatibility_client_connect_callback', addr)
    return 0


def _inincompatibility_client_close_callback(addr) -> int:
    print('_inincompatibility_client_close_callback', addr)
    return 0


def time_out(t: float):
    tl = time.time()
    time.sleep(t)
    tr = time.time()
    return tr, tl
