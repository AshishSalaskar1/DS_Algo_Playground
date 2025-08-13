# Composite (Structural)

Ref: https://refactoring.guru/design-patterns/composite

Overview
- Treat individual objects and compositions of objects uniformly.
- Build tree structures with a common interface for leaves and composites.

When to use
- You need to work with a tree of objects and perform operations uniformly.

How to identify
- Shared component interface. Composite stores children; Leaf has no children.

Pros
- Simplifies client code by treating leaf and composite similarly.
- Easy to add new component types.

Cons
- Can make code harder to constrain (e.g., certain ops valid only on leaves).

Common confusions
- vs Decorator: Both are recursive composition; Decorator adds responsibilities, Composite forms part-whole trees.

Python example (filesystem-like tree)
```python
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

    print(root.size())  # 2148
```

Quick glance
- Same interface for leaf and composite.
- Operations recurse over the tree.
