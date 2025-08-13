# Observer (Behavioral)

Ref: https://refactoring.guru/design-patterns/observer

Overview
- Define a subscription mechanism to notify multiple objects about events happening to the subject.

When to use
- One-to-many dependencies; GUI, events, data streams.

How to identify
- Subject keeps a list of observers and notifies them on changes.

Pros
- Loose coupling between subject and observers.
- Supports dynamic subscriptions.

Cons
- Unexpected updates order; potential memory leaks if not unsubscribed.

Common confusions
- vs Pub/Sub: Observer is often in-process and direct; Pub/Sub can be brokered/remote.

Python example
```python
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
```

Quick glance
- Subject manages observers; call update() on changes.
