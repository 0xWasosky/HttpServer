from utils.response import Response


class Cache:
    cache = {}

    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

    def add(self, hash_string: str,response: Response) -> None:
        if len(self.cache) < self.max_size: 
            self.cache[hash_string] = response
    
    def clear(self):
        self.cache = {}
    
    def get(self, hash_string: str) -> Response | None:
        return self.cache.get(hash_string)