# Flyweight (Structural)

Ref: https://refactoring.guru/design-patterns/flyweight

Overview
- Shares common state between many objects to save memory.
- Split state into intrinsic (shared) and extrinsic (context-specific) parts.

When to use
- You have lots of similar small objects (e.g., characters in a text editor, map tiles).

How to identify
- A factory/registry returns shared immutable objects (flyweights) based on a key.

Pros
- Significant memory savings.
- Can speed up creation.

Cons
- Complexity of managing extrinsic state.
- Thread-safety concerns for shared objects.

Common confusions
- vs Prototype: Prototype clones new objects; Flyweight reuses shared instances.

Python example (tree rendering)
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class TreeType:
    name: str
    color: str
    texture: str

class TreeFactory:
    _cache: dict[tuple[str, str, str], TreeType] = {}

    @classmethod
    def get_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._cache:
            cls._cache[key] = TreeType(*key)
        return cls._cache[key]

@dataclass
class Tree:
    x: int
    y: int
    type: TreeType  # intrinsic shared

class Forest:
    def __init__(self) -> None:
        self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        ttype = TreeFactory.get_type(name, color, texture)
        self._trees.append(Tree(x, y, ttype))

if __name__ == "__main__":
    forest = Forest()
    for i in range(10000):
        forest.plant_tree(i % 100, i // 100, "Oak", "Green", "rough")
    # Only 1 TreeType for Oak/Green/rough
    print(len(TreeFactory._cache))  # 1
```

Quick glance
- Cache immutable shared state; pass per-object state externally.
- Great for huge numbers of similar objects.
