from __future__ import annotations
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, nxt: "Handler") -> "Handler":
        self._next = nxt
        return nxt

    def handle(self, request: dict) -> str | None:
        if self._next:
            return self._next.handle(request)
        return None

class Level1(Handler):
    def handle(self, request: dict) -> str | None:
        if request.get("severity") == 1:
            return "L1 resolved"
        return super().handle(request)

class Level2(Handler):
    def handle(self, request: dict) -> str | None:
        if request.get("severity") == 2:
            return "L2 resolved"
        return super().handle(request)

class Manager(Handler):
    def handle(self, request: dict) -> str | None:
        if request.get("severity") >= 3:
            return "Manager resolved"
        return super().handle(request)

if __name__ == "__main__":
    l1 = Level1(); l2 = Level2(); mgr = Manager()
    l1.set_next(l2).set_next(mgr)
    print(l1.handle({"severity": 2}))
