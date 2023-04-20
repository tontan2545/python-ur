import socket


class Arm:
    _ip: str = "10.10.0.14"
    _port: int = 30003
    _client: socket.socket
    x: float = 0
    y: float = 0
    z: float = 0
    rx: float = 0
    ry: float = 0
    rz: float = 0

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f"Connecting to arm at {self._ip}:{self._port}...")
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print("Connected to arm.")

    def get_position(self):
        self._client.send(b"GET POS\n")
        response = str(self._client.recv(255), "UTF-8")
        print(response)
