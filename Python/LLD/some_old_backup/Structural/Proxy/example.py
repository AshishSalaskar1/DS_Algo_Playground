from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self) -> None: ...

class RealImage(Image):
    def __init__(self, path: str) -> None:
        self.path = path
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        print(f"Loading {self.path} from disk...")

    def display(self) -> None:
        print(f"Displaying {self.path}")

class ProxyImage(Image):
    def __init__(self, path: str) -> None:
        self.path = path
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage(self.path)
        self._real.display()

if __name__ == "__main__":
    img = ProxyImage("photo.png")
    img.display()
    img.display()
