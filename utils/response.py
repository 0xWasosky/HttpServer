import os
import zlib
from utils.status_code import StatusCodes

"""

Body

The last part of a response is the body. Not all responses have one: responses with a status code that sufficiently answers the request without the need for corresponding payload (like 201 Created or 204 No Content) usually don't.

Bodies can be broadly divided into three categories:

    Single-resource bodies, consisting of a single file of known length, defined by the two headers: Content-Type and Content-Length.
    Single-resource bodies, consisting of a single file of unknown length, encoded by chunks with Transfer-Encoding set to chunked.
    Multiple-resource bodies, consisting of a multipart body, each containing a different section of information. These are relatively rare.

"""

# da applicare il packing = chunck per chunck
# on response

class Response:
    @staticmethod
    def base_response(protocol: str, status: StatusCodes | int, headers: dict, body: str):
        response = b""

        response += protocol.encode() + " ".encode() + str(status).encode()# line 1
        response += '\n'.encode()
        for key, value in headers.items():
            response += f"{key}: {value}".encode() + '\n'.encode()
        
        response += "\n\n".encode()
        response += body.encode()
        return response


def compile_packing_body(dir_: str):
    body = b""


    for file in os.listdir(dir_):
        with open(f"{dir_}/{file}", 'rb') as f:
            body += f"{file}:{zlib.compress(f.read()).decode()}".encode()

    return body

