import socket


class Gripper:
    _ip: str = "10.10.0.14"
    _port: int = 63352
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f"Connecting to gripper at {self._ip}:{self._port}...")
        self.__connect()

    def __connect(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print("Connected to gripper. Getting ACT")
        self._client.send(b"GET ACT\n")
        if "1" in str(self._client.recv(10), "UTF-8"):
            print("ACT Received. Activating gripper")

    def open(self):
        self._client.send(b"SET POS 0\n")
        print(str(self._client.recv(255), "UTF-8"))

    def close(self):
        self._client.send(b"SET POS 255\n")
        print(str(self._client.recv(255), "UTF-8"))
