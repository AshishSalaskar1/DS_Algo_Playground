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
    type: TreeType

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
    print(len(TreeFactory._cache))
