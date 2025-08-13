# Decorator (Structural)

Ref: https://refactoring.guru/design-patterns/decorator

Overview
- Attach additional responsibilities to an object dynamically by wrapping it.
- Alternative to subclassing for extending behavior.

When to use
- You need to add cross-cutting features (logging, caching, auth) without changing the original class.
- You want many combinations of features at runtime.

How to identify
- A wrapper with the same interface that holds a reference to the wrapped component and delegates.

Pros
- Compose behaviors dynamically.
- Adheres to Open/Closed; avoids heavy inheritance.

Cons
- Many small objects; debugging can be harder.

Common confusions
- vs Adapter: Decorator keeps interface, adds behavior; Adapter converts interface.
- vs Proxy: Proxy controls access; Decorator adds responsibilities.

Python example (notifier with decorators)
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrappee: Notifier) -> None:
        self.wrappee = wrappee

    def send(self, message: str) -> None:
        self.wrappee.send(message)

class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"SMS: {message}")

class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"Slack: {message}")

if __name__ == "__main__":
    notifier: Notifier = EmailNotifier()
    notifier = SMSDecorator(NotifierDecorator(notifier))
    notifier = SlackDecorator(notifier)
    notifier.send("Build finished")
```

Quick glance
- Wrap object with same interface; delegate then add behavior.
- Stack multiple decorators for combined features.
