import socket
from utils import Response, Request, StatusCodes


routes = {}


def route(path):
    def wrapper(func):
        routes[path] = func

    return wrapper


class Pack:
    def __init__(self, host: str, port: int, max_connections: int) -> None:
        self.host = host
        self.port = port
        self.max_connections = max_connections

    def __handler(self):
        while True:
            connection, _ = self.sock.accept()

            self.__connection(connection)

    def __connection(self, connection):
        try:

            request = Request(connection.recv(1024))
            print(request.headers)

            connection.send(routes[request.path]())
            connection.close()
        except:
            error = Response.base_response(
                protocol="HTTP/1.1",
                status=StatusCodes.internal_server_error,
                headers={"Content-type": "text;html"},
                body="<h1>Internal server error</h1>",
            )
            connection.send(error)
            connection.close()

    def run(self):

        print(f"http://{self.host}:{self.port}")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.max_connections)
        self.__handler()
