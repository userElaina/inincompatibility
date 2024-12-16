import socket
import pickle


def _pass_return_0(addr):
    '''
    >>> _pass_return_0(addr: Tuple[str, int] | Any) -> int
    '''
    return 0


class IServer:
    def __init__(
        self,
        addr=('0.0.0.0', 0),
        family=socket.AF_INET,
        buffer_size=4096,
        listen_n=1,
        verbose=False
    ):
        '''
        >>> IServer(
                addr: Tuple[str, int] | Any = ('0.0.0.0', 0),
                family: int = socket.AF_INET,
                buffer_size: int = 4096,
                listen_n: int = 1,
                verbose: bool = False
            ) -> IServer
        '''
        self.family = family
        self.buffer_size = buffer_size
        self.verbose = verbose

        self.server = socket.socket(family, socket.SOCK_STREAM)
        self.server.bind(addr)
        self.addr = self.server.getsockname()
        assert listen_n == 1  # todo: support multiple clients
        self.server.listen(listen_n)

        self.client_connect_callback = _pass_return_0
        self.client_close_callback = _pass_return_0
        self.func_name = dict()
        self.add_func(eval, '_inincompatibility_remote_eval')
        self.add_func(exec, '_inincompatibility_remote_exec')

    def _eval_from_data(self, b):
        '''
        >>> _eval_from_data(b: bytes) -> bytes
        '''
        func, args, kwargs = pickle.loads(b)
        assert isinstance(func, str)
        assert isinstance(args, tuple)
        assert isinstance(kwargs, dict)
        assert func in self.func_name
        if self.verbose:
            print('_eval', func, args, kwargs)
        try:
            res = self.func_name[func](*args, **kwargs)
        except Exception as e:
            res = e
        return pickle.dumps(res)

    def add_func(self, func, name=None, errors='strict'):
        '''
        >>> add_func(
                func: Callable,
                name: str = None,
                errors: Literal['ignore', 'replace', 'strict'] = 'ignore'
            ) -> None
        '''
        # 'ignore' 'replace' 'strict'
        assert callable(func)
        if name is None:
            name = func.__name__
        if name in self.func_name:
            print('Warning: Function name "%s" already exists' % name)
            if errors == 'ignore':
                return
            elif errors == 'replace':
                pass
            elif errors == 'strict':
                raise ValueError('Function name "%s" already exists' % name)
            else:
                raise ValueError('Invalid value for `errors`')
        if self.verbose:
            print('_add_func', name, func)
        self.func_name[name] = func

    def add_funcs(self, *args):
        '''
        >>> add_funcs(
                *args: Callable | Iterable[Callable]
            ) -> None
        '''
        for fs in args:
            if isinstance(fs, (list, tuple)):
                for f in fs:
                    self.add_func(f)
            else:
                self.add_func(fs)

    def join_client(self):
        '''
        >>> join_client() -> int
        '''
        client_socket, client_addr = self.server.accept()
        print('Connected by', client_addr)
        if self.client_connect_callback(client_addr):
            client_socket.close()
            print('Closed by', client_addr)
            return self.client_close_callback(client_addr)
        while True:
            data = client_socket.recv(self.buffer_size)
            if not data:
                break
            res = self._eval_from_data(data)
            client_socket.sendall(res)
        client_socket.close()
        print('Closed by', client_addr)
        return self.client_close_callback(client_addr)

    def join(self):
        '''
        >>> join() -> None
        '''
        print('Server started at', self.addr)
        # print('Now you can connect to this server.')
        while True:
            self.join_client()
        self.close()

    def run(self):
        '''
        >>> run() -> None
        '''
        self.join()

    def close(self):
        '''
        >>> close() -> None
        '''
        return self.server.close()

    def gen_import_code(self, p='to_import.py', addr=None):
        '''
        >>> gen_import_code(
                p: str = 'to_import.py',
                addr: Tuple[str, int] | Any = None
            ) -> str
        '''

        family = self.family
        if addr is None:
            addr = self.addr
        if family == socket.AF_INET:
            assert len(addr) == 2
            host, port = addr
            if host == '0.0.0.0':
                host = '127.0.0.1'
            if port == 0:
                port = self.addr[1]
            addr = (host, port)
        elif family == socket.AF_INET6:
            assert 2 <= len(addr) <= 4
            _addr = list(addr)
            if _addr[0] == '::':
                _addr[0] = '::1'
            if _addr[1] == 0:
                _addr[1] = self.addr[1]
            addr = tuple(_addr)

        generated_script = '''# Generated by `inincompatibility`.
# **Not** depend on `incompatibility`. :)
# You can directly `import` this file in another environment.
import socket
import pickle\n
BUFFER_SIZE = ''' + str(self.buffer_size) + '''\n
client = socket.socket(''' + str(family) + ''', socket.SOCK_STREAM)
client.connect(''' + str(addr) + ''')\n\n
def _func_eval(func, args, kwargs):
    data = pickle.dumps((func, args, kwargs))
    client.sendall(data)
    return pickle.loads(client.recv(BUFFER_SIZE))\n'''
        for name in self.func_name:
            generated_script += '''\n
def ''' + name + '''(*args, **kwargs):
    return _func_eval(\'''' + name + '''\', args, kwargs)\n'''

        import os
        if os.path.exists(p):
            # raise FileExistsError('File already exists')
            pass
        else:
            os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
        with open(p, 'wb') as f:
            f.write(generated_script.encode('utf-8'))
        print('Generated at:', repr(p))
        return p
