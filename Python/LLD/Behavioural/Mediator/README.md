# Mediator (Behavioral)

Ref: https://refactoring.guru/design-patterns/mediator

Overview
- Defines an object that encapsulates how a set of objects interact, reducing direct dependencies.

When to use
- Complex interactions between many objects cause tight coupling.

How to identify
- Colleagues communicate indirectly via a mediator object.

Pros
- Reduces coupling and centralizes communication logic.
- Easier to modify interactions.

Cons
- Mediator can become complex/god-object.

Common confusions
- vs Observer: Mediator coordinates bi-directional interactions; Observer broadcasts one-to-many notifications.

Python example (dialog controls)
```python
from __future__ import annotations
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None: ...

class Dialog(Mediator):
    def __init__(self) -> None:
        self.login = TextBox(self)
        self.password = TextBox(self)
        self.button = Button(self)

    def notify(self, sender: object, event: str) -> None:
        if sender is self.login and event == "text_changed":
            self.button.enabled = bool(self.login.text and self.password.text)
        if sender is self.password and event == "text_changed":
            self.button.enabled = bool(self.login.text and self.password.text)
        if sender is self.button and event == "click":
            print("Submitting:", self.login.text)

class Component:
    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator

class TextBox(Component):
    def __init__(self, mediator: Mediator) -> None:
        super().__init__(mediator)
        self.text = ""

    def input(self, value: str) -> None:
        self.text = value
        self.mediator.notify(self, "text_changed")

class Button(Component):
    def __init__(self, mediator: Mediator) -> None:
        super().__init__(mediator)
        self.enabled = False

    def click(self) -> None:
        if self.enabled:
            self.mediator.notify(self, "click")

if __name__ == "__main__":
    d = Dialog()
    d.login.input("ash")
    d.password.input("secret")
    d.button.click()
```

Quick glance
- Centralize communication in a mediator.
- Colleagues are simpler and loosely coupled.
