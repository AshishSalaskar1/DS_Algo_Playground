# Abstract Factory (Creational)

Ref: https://refactoring.guru/design-patterns/abstract-factory

Overview
- Provides an interface for creating families of related objects without specifying their concrete classes.
- Ensures products created together are compatible.

When to use
- Your system needs to work with multiple product families (e.g., Windows/Mac UI) and you want to switch families at runtime.
- You must enforce that objects from the same family are used together.

How to identify
- A factory interface creates multiple related products.
- Concrete factories produce a consistent set of products that work together.

Pros
- Ensures product compatibility.
- Isolates concrete classes and simplifies switching families.
- Supports the Open/Closed Principle for adding new families.

Cons
- Harder to support new product types since all factories must change.
- More complexity and classes.

Common confusions
- vs Factory Method: AF creates entire families; FM creates one product type.
- vs Builder: Builder assembles one complex product step-by-step; AF creates multiple related products.

Python example (cross-platform UI)
```python
from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...

class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str: ...

# Concrete Products
class WinButton(Button):
    def render(self) -> str:
        return "Windows Button"

class MacButton(Button):
    def render(self) -> str:
        return "MacOS Button"

class WinCheckbox(Checkbox):
    def check(self) -> str:
        return "Windows Checkbox"

class MacCheckbox(Checkbox):
    def check(self) -> str:
        return "MacOS Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...

# Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client
class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def draw(self) -> None:
        print(self.button.render())
        print(self.checkbox.check())

if __name__ == "__main__":
    factory: GUIFactory = MacFactory()
    app = Application(factory)
    app.draw()
```

Quick glance
- One factory creates many related products.
- Swap the entire family by switching the factory.
- Keeps UI consistent across platforms.
