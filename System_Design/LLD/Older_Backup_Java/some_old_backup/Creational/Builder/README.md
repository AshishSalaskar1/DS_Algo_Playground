# Builder (Creational)

Ref: https://refactoring.guru/design-patterns/builder

Overview
- Separates the construction of a complex object from its representation.
- The same construction steps can create different representations.

When to use
- Building complex objects with many optional parts or configurations.
- You want the construction process to be independent from the final object.

How to identify
- A Director orchestrates building steps.
- A Builder interface defines steps; Concrete Builders implement and produce Products.

Pros
- Step-by-step construction with control over creation.
- Reuse building process for different representations.
- Avoids telescoping constructors.

Cons
- More classes and indirection than direct construction.

Common confusions
- vs Abstract Factory: AF creates families of related products; Builder creates one complex product.
- vs Factory Method: FM returns one product in a single call; Builder runs multiple steps then returns the product.

Python example (pizza builder)
```python
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
        # margherita stays simple; ignore or record
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

    # Or custom build without a director
    custom = (
        MargheritaBuilder()
        .size("small")
        .add_cheese()
        .add_veggie("olives")
        .add_veggie("basil")
        .build()
    )
    print(custom)
```

Quick glance
- Director orchestrates steps; Builders change the parts.
- Good for complex construction with many options.
- Product is returned via build().
