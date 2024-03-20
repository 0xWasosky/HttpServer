# Http Server




## Example


```py
from pack import route, Pack, Response


app = Pack("127.0.0.1", 5000, 1)


@route("/")
def index():
    return Response.base_response(
        protocol="HTTP/1.1",
        status=200,
        headers={"Content-type": "text;html"},
        body="<h1>Hi im a http server</h1>",
    )


if __name__ == "__main__":
    app.run()

```

