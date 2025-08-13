# Template Method (Behavioral)

Ref: https://refactoring.guru/design-patterns/template-method

Overview
- Defines the skeleton of an algorithm in a base class, deferring some steps to subclasses.

When to use
- Several classes share the same high-level algorithm with varying steps.

How to identify
- Base class provides a template method calling abstract/overridable steps.

Pros
- Reuse algorithm skeleton while allowing variation.

Cons
- Inheritance-based; variations are compile-time.

Common confusions
- vs Strategy: Strategy uses composition to swap behavior at runtime; Template uses inheritance.

Python example
```python
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
```

Quick glance
- Base method defines steps; subclasses fill in parts.
