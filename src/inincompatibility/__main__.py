import argparse
from .iserver import IServer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        'inincompatibility',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input',
        help='Original Python file to analyze',
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

    a = parser.parse_args()
    _input = a.input
    _output = a.output
    _ip, _port = a.addr.split(':')
    _addr = (_ip, int(_port))
    _buffersize = a.buffersize
    _verbose = a.verbose

    inincs = IServer(
        addr=_addr,
        buffer_size=_buffersize,
        verbose=_verbose
    )

    with open(_input, 'rb') as f:
        _b = f.read()
        if not _output:
            _output = _input
            _input = _output + '.ininc_bak.py'
            open(_input, 'wb').write(_b)
        _s = _b.decode('utf-8')
        exec(_s)
        for s in _s.strip().split('\n'):
            # only supports one-line `from ... import ...` statement
            s = s.strip()
            if s.startswith('from ') and '*' not in s:
                assert ' import ' in s
                if _verbose:
                    print('Analyze line:', repr(s))
                if ' as ' in s:
                    s = s.split(' as ')[1]
                else:
                    s = s.split(' import ')[1]
                for i in s.split(','):
                    name = i.strip()
                    func = eval(name)
                    if name == '_inincompatibility_client_connect_callback':
                        inincs.client_connect_callback = func
                        if _verbose:
                            print('Overload client_connect_callback:', func)
                    elif name == '_inincompatibility_client_close_callback':
                        inincs.client_close_callback = func
                        if _verbose:
                            print('Overload client_close_callback:', func)
                    else:
                        if callable(func):
                            inincs.add_func(func, name, 'replace')
                        elif _verbose:
                            print('Skip:', func)

    inincs.gen_import_code(_output)
    inincs.run()
