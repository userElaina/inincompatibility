from lib1 import getdata, calc
from inincompatibility import IServer

iics = IServer(debug=True)
iics.add_funcs(getdata, calc)
iics.gen_import_code()
iics.run()
