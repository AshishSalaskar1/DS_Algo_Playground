from abc import ABC, abstractmethod

class DataParser(ABC):
    def parse(self, path: str) -> dict:
        raw = self.read(path)
        data = self.decode(raw)
        return self.normalize(data)

    @abstractmethod
    def read(self, path: str) -> bytes: ...

    @abstractmethod
    def decode(self, raw: bytes) -> dict: ...

    def normalize(self, data: dict) -> dict:
        return data

class JSONParser(DataParser):
    def read(self, path: str) -> bytes:
        return b'{"x":1}'

    def decode(self, raw: bytes) -> dict:
        import json
        return json.loads(raw)

if __name__ == "__main__":
    p = JSONParser()
    print(p.parse("/tmp/a.json"))
