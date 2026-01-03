from abc import ABC, abstractmethod

class FSNode(ABC):
    @abstractmethod
    def size(self) -> int: ...

class File(FSNode):
    def __init__(self, name: str, size_bytes: int) -> None:
        self.name = name
        self._size = size_bytes

    def size(self) -> int:
        return self._size

class Directory(FSNode):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: list[FSNode] = []

    def add(self, node: FSNode) -> None:
        self._children.append(node)

    def size(self) -> int:
        return sum(child.size() for child in self._children)

if __name__ == "__main__":
    root = Directory("root")
    root.add(File("a.txt", 100))
    pics = Directory("pics")
    pics.add(File("img.jpg", 2048))
    root.add(pics)

    print(root.size())
