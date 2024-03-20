class Request:
    def __init__(self, data: bytes) -> None:
        self.request = data.decode()
        self.lines = self.request.splitlines()

    @property
    def path(self):
        return self.lines[0].split()[1]

    @property
    def method(self):
        return self.lines[0].split()[0]

    @property
    def headers(self):
       headers = {}

       for data in self.lines[1:]:
           if data == "\n\n":
               break
           split = data.split(":")
           if len(split) == 2:
               headers[split[0]] = split[1]
       return headers

    @property
    def payload(self):
        if not self.method in ("POST", "PUT", "PATCH"): 
            return None
 
        return "".join(s for s in self.lines[len(self.headers) + 3:])
