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

    def get_position(self):
        self._client.send(b"get_actual_tcp_pose()\n")
        print(self._client.recv(1024).decode("unicode_escape"))
        # print(response)

    def set_zero(self, move_option="movej"):
        # TODO: set to desired home position
        # Does not work, do not run this!
        move_cmd = f"{move_option}(p[163,-327,-417,0,-3,0],a=1.4,v=1.05)"
        self.__send(move_cmd)

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
        self._client.send(move_cmd.encode(encoding="utf-8", errors="ignore"))

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
        self._client.send(move_cmd.encode(encoding="utf-8", errors="ignore"))


if __name__ == "__main__":
    arm = Arm()
    arm.get_position()
