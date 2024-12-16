import socket
import pickle


class IClient:
    def __init__(self, addr, family=socket.AF_INET, buffer_size=4096):
        '''
        >>> IClient(
                addr: Tuple[str, int] | Any,
                family: int = socket.AF_INET,
                buffer_size: int = 4096
            ) -> IClient
        '''
        self.family = family
        self.buffer_size = buffer_size
        self.client = socket.socket(family, socket.SOCK_STREAM)
        self.client.connect(addr)

    def func_eval(self, func, args, kwargs):
        '''
        >>> func_eval(func: Callable, args: Tuple, kwargs: Dict) -> Any
        '''
        data = pickle.dumps((func, args, kwargs))
        self.client.sendall(data)
        return pickle.loads(self.client.recv(self.buffer_size))
