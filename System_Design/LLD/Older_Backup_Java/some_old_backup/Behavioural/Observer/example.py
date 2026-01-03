from __future__ import annotations
from typing import Protocol, List

class Observer(Protocol):
    def update(self, data: str) -> None: ...

class Subject:
    def __init__(self) -> None:
        self._subs: List[Observer] = []

    def subscribe(self, obs: Observer) -> None:
        self._subs.append(obs)

    def unsubscribe(self, obs: Observer) -> None:
        self._subs.remove(obs)

    def notify(self, data: str) -> None:
        for obs in list(self._subs):
            obs.update(data)

class ConsoleObserver:
    def update(self, data: str) -> None:
        print("Observed:", data)

if __name__ == "__main__":
    subject = Subject()
    sub = ConsoleObserver()
    subject.subscribe(sub)
    subject.notify("event#1")
