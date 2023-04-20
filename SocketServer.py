import socket
import ast


class Server:
    HOST: str = socket.gethostbyname(socket.gethostname())
    PORT: int = 503
    _server: socket.socket

    def __init__(self, host: str = None, port: int = None) -> None:
        self.HOST = host or self.HOST
        self.PORT = port or self.PORT
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind((self.HOST, self.PORT))

    def listen(self, func: callable) -> None:
        self._server.listen()
        print(f"Server listening at {self.HOST}:{self.PORT}")
        while True:
            conn, addr = self._server.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    func(data.decode("UTF-8"))
                print(f"Disconnected by {addr}")


if __name__ == "__main__":
    s = Server(port=3000)

    @s.listen
    def handle_message(msg: str):
        processed_msg = ast.literal_eval(msg)
        if isinstance(processed_msg, tuple):
            print(processed_msg)
