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
        pass

    def plan_delivery(self, cargo: str) -> None:
        transport = self.create_transport()
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
