import argparse
from .iserver import IServer
from . import VERSION

if __name__ == "__main__":
    print('Thanks for using inincompatibility', VERSION)
    parser = argparse.ArgumentParser(
        'inincompatibility',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input',
        help='Original Python code to analyze',
        type=str,
        default='to_import.py'
    )
    parser.add_argument(
        '-o', '--output',
        help='Generated Python file that can be imported',
        type=str,
        default=''
    )
    parser.add_argument(
        '-a', '--addr',
        help='ip:port',
        type=str,
        default='0.0.0.0:0'
    )
    parser.add_argument(
        '--clientaddr',
        help='ip:port',
        type=str,
        default=None
    )
    parser.add_argument(
        '--buffersize',
        help='Buffer size',
        type=int,
        default=1048576
    )
    parser.add_argument(
        '--verbose',
        help='Verbose mode',
        action='store_true'
    )
    parser.add_argument(
        '--inputcode',
        help='Input code directly',
        action='store_true'
    )

    a = parser.parse_args()
    _input = a.input
    _output = a.output

    host, port = a.addr.rsplit(':', 1)
    addr = (host, int(port))
    if a.clientaddr is None:
        clientaddr = None
    else:
        host, port = a.clientaddr.rsplit(':', 1)
        clientaddr = (host, int(port))
    buffer_size = a.buffersize
    verbose = a.verbose
    _input_code = a.inputcode

    inincs = IServer(
        addr=addr,
        buffer_size=buffer_size,
        verbose=verbose
    )

    if _input_code:
        _s = _input
        exec(_s)
        lines = _s.strip().split(';')
    else:
        f = open(_input, 'rb')
        _b = f.read()
        f.close()
        _s = _b.decode('utf-8')
        exec(_s)
        if not _output:
            _output = _input
            _input = _output + '.ininc_bak.py'
            open(_input, 'wb').write(_b)
        lines = _s.strip().split('\n')

    for line in lines:
        # only supports one-line `from ... import ...` statement
        line = line.strip()
        if line.startswith('from ') and '*' not in line:
            assert ' import ' in line
            if verbose:
                print('Analyze line:', repr(line))
            if ' as ' in line:
                line = line.split(' as ')[1]
            else:
                line = line.split(' import ')[1]
            for i in line.split(','):
                name = i.strip()
                func = eval(name)
                if name == '_inincompatibility_client_connect_callback':
                    inincs.client_connect_callback = func
                    if verbose:
                        print('Overload client_connect_callback:', func)
                elif name == '_inincompatibility_client_close_callback':
                    inincs.client_close_callback = func
                    if verbose:
                        print('Overload client_close_callback:', func)
                else:
                    if callable(func):
                        inincs.add_func(func, name, 'replace')
                    elif verbose:
                        print('Skip:', func)

    inincs.gen_import_code(_output, clientaddr)
    inincs.run()
