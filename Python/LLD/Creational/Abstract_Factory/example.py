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
