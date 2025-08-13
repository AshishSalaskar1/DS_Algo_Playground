from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

@dataclass
class Pizza:
    size: str
    cheese: bool = False
    pepperoni: bool = False
    veggies: List[str] = field(default_factory=list)

# Builder interface
class PizzaBuilder(ABC):
    @abstractmethod
    def size(self, size: str) -> "PizzaBuilder": ...

    @abstractmethod
    def add_cheese(self) -> "PizzaBuilder": ...

    @abstractmethod
    def add_pepperoni(self) -> "PizzaBuilder": ...

    @abstractmethod
    def add_veggie(self, name: str) -> "PizzaBuilder": ...

    @abstractmethod
    def build(self) -> Pizza: ...

# Concrete Builder
class MargheritaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self._size = "medium"
        self._cheese = False
        self._pepperoni = False
        self._veggies: List[str] = []

    def size(self, size: str) -> "PizzaBuilder":
        self._size = size
        return self

    def add_cheese(self) -> "PizzaBuilder":
        self._cheese = True
        return self

    def add_pepperoni(self) -> "PizzaBuilder":
        self._pepperoni = False
        return self

    def add_veggie(self, name: str) -> "PizzaBuilder":
        self._veggies.append(name)
        return self

    def build(self) -> Pizza:
        return Pizza(self._size, self._cheese, self._pepperoni, self._veggies)

# Director (optional)
class Chef:
    def make_simple_margherita(self, builder: PizzaBuilder) -> Pizza:
        return builder.size("large").add_cheese().build()

if __name__ == "__main__":
    chef = Chef()
    pizza = chef.make_simple_margherita(MargheritaBuilder())
    print(pizza)

    custom = (
        MargheritaBuilder()
        .size("small")
        .add_cheese()
        .add_veggie("olives")
        .add_veggie("basil")
        .build()
    )
    print(custom)
