import socket
import struct


class Arm:
    _ip: str = "10.10.0.14"
    _port: int = 30003
    _client: socket.socket

    def __init__(self, ip: str = None, port: int = None) -> None:
        self._port = port or self._port
        self._ip = ip or self._ip
        print(f"Connecting to arm at {self._ip}:{self._port}...")
        self.__connect()

    def __connect(self) -> None:
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self._ip, self._port))
        print("Connected to arm.")

    def __send(self, cmd: str):
        self._client.send(f"{cmd}\n".encode(encoding="utf-8", errors="ignore"))

    def movej(
        self,
        x: float = None,
        y: float = None,
        z: float = None,
        rx: float = None,
        ry: float = None,
        rz: float = None,
    ):
        move_cmd = f"movej(pose_add(get_actual_tcp_pose(),p[{x or 0},{y or 0},{z or 0},{rx or 0},{ry or 0},{rz or 0}]),a=1.4,v=1.05)\n"
        self.__send(move_cmd)

    def movel(
        self,
        x: float = None,
        y: float = None,
        z: float = None,
        rx: float = None,
        ry: float = None,
        rz: float = None,
    ):
        move_cmd = f"movel(pose_add(get_actual_tcp_pose(),p[{x or 0},{y or 0},{z or 0},{rx or 0},{ry or 0},{rz or 0}]),a=1.4,v=1.05)\n"
        self.__send(move_cmd)


if __name__ == "__main__":
    arm = Arm()
