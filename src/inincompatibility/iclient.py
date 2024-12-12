import socket
import pickle


class IClient:
    def __init__(self, addr, buffer_size=4096):
        '''
        >>> IClient(addr: Tuple[str, int], buffer_size: int = 4096) -> None
        '''
        self.buffer_size = buffer_size
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)

    def func_eval(self, func, args, kwargs):
        '''
        >>> func_eval(func: Callable, args: Tuple, kwargs: Dict) -> Any
        '''
        data = pickle.dumps((func, args, kwargs))
        self.client.sendall(data)
        return pickle.loads(self.client.recv(self.buffer_size))
