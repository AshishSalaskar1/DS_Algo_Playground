# Factory Method (Creational)

Ref: https://refactoring.guru/design-patterns/factory-method

Overview
- Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
- Moves object creation to subclasses, keeping the base class focused on logic.

When to use
- A base class can’t know which concrete class it should instantiate.
- You want to decouple product creation from usage and make it easy to add new product types.

How to identify
- A base “creator” class defines a factory method that returns an abstract/product type.
- Subclasses override this method to return different concrete products.

Pros
- Single Responsibility: separates product creation from business logic.
- Open/Closed: add new products via new subclasses without changing existing code.
- Testability: override the factory method to inject test doubles.

Cons
- More classes and indirection.
- Might be overkill if creation is simple.

Common confusions
- Factory Method vs Abstract Factory: FM creates a single product; AF creates related product families.
- Factory Method vs Builder: Builder constructs complex objects step-by-step; FM returns a ready product.

Python example
```python
from abc import ABC, abstractmethod

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self, cargo: str) -> None:
        pass

class Truck(Transport):
    def deliver(self, cargo: str) -> None:
        print(f"Delivering {cargo} by road in a truck")

class Ship(Transport):
    def deliver(self, cargo: str) -> None:
        print(f"Delivering {cargo} by sea in a ship")

# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        """Factory Method returning an abstract product."""
        pass

    def plan_delivery(self, cargo: str) -> None:
        transport = self.create_transport()  # defer to subclass
        # delivery workflow can remain unchanged for all transports
        transport.deliver(cargo)

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

if __name__ == "__main__":
    logistics: Logistics = RoadLogistics()
    logistics.plan_delivery("Books")

    logistics = SeaLogistics()
    logistics.plan_delivery("Containers")
```

Quick glance
- Base class declares factory method; subclasses choose product.
- Swap product types at runtime by using a different creator subclass.
- Reduces coupling between clients and concrete classes.
