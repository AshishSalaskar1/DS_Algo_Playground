# Proxy (Structural)

Ref: https://refactoring.guru/design-patterns/proxy

Overview
- Provides a surrogate or placeholder to control access to another object.
- Adds lazy-loading, caching, access control, logging, etc.

When to use
- Expensive or remote object access should be controlled or optimized.

How to identify
- A class implements the same interface as the real subject and holds a reference to it.

Pros
- Add non-functional concerns transparently.
- Can protect, cache, or lazy-load the real subject.

Cons
- Adds indirection and potential complexity.

Common confusions
- vs Decorator: both wrap; Proxy focuses on control/access; Decorator adds behavior.

Python example (virtual proxy for image loading)
```python
from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self) -> None: ...

class RealImage(Image):
    def __init__(self, path: str) -> None:
        self.path = path
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        print(f"Loading {self.path} from disk...")

    def display(self) -> None:
        print(f"Displaying {self.path}")

class ProxyImage(Image):
    def __init__(self, path: str) -> None:
        self.path = path
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage(self.path)
        self._real.display()

if __name__ == "__main__":
    img = ProxyImage("photo.png")
    img.display()  # loads on first call
    img.display()  # reuses
```

Quick glance
- Same interface; controls access to heavy/remote object.
- Good for lazy-load, cache, logging, auth.
