import sys
import time
from to_import import _inincompatibility_remote_exec
from to_import import _inincompatibility_remote_eval, time_out
from to_import import time_out

assert sys.version_info.minor <= 9
_inincompatibility_remote_exec('import sys; print(__file__, sys.version_info.minor)')
print(sys.version_info.minor, _inincompatibility_remote_eval(
    '__import__(\'sys\').version_info.minor'
))

s = 2.
otl = time.time()
tr, tl = time_out(s)
otr = time.time()
print(tl - otl, tr - tl - s, otr - tr)
