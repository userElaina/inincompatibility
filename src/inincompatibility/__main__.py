import argparse
from .iserver import IServer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        'inincompatibility',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input',
        help='Original file to `import`',
        default='to_import.py'
    )
    parser.add_argument(
        '-o', '--output',
        help='Generated file to `import`',
        default=''
    )
    a = parser.parse_args()
    p = a.input
    op = a.output

    iics = IServer(debug=False)

    with open(p, 'rb') as f:
        _b = f.read()
        _s = _b.decode('utf-8')
        if not op:
            op = p
            p = op + '.bak'
            open(p, 'wb').write(_b)
        exec(_s)
        _l = _s.strip().split('\n')
        for s in _l:
            flg1 = s.startswith('from ') and ' import ' in s
            flg2 = s.startswith('import ')
            if flg1 or flg2:
                if ' as ' in s:
                    s = s.split(' as ')[1]
                else:
                    s = s.split(' import ')[1]
                funcs = [eval(i.strip()) for i in s.split(', ')]
                iics.add_funcs(funcs)

    iics.gen_import_code(op)
    iics.run()
