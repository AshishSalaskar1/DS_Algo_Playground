# Prototype (Creational)

Ref: https://refactoring.guru/design-patterns/prototype

Overview
- Create new objects by copying existing ones (prototypes) instead of instantiating from scratch.
- Useful when object creation is expensive or complex.

When to use
- You need to avoid costly initialization for similar objects.
- You want to keep runtime copies that can be tweaked independently.

How to identify
- Classes implement a clone/copy method.
- Often uses a registry of prototypes to create copies.

Pros
- Avoids subclass explosion for object configuration.
- Faster creation via cloning.
- Can clone objects without exposing their internals.

Cons
- Deep vs shallow copy complexity.
- Cloning complex object graphs can be tricky.

Common confusions
- vs Factory Method/Abstract Factory: those create new instances via constructors; Prototype clones existing ones.

Python example
```python
import copy
from dataclasses import dataclass

@dataclass
class Document:
    title: str
    body: list[str]
    metadata: dict

    def clone(self) -> "Document":
        # deep copy to decouple nested structures
        return copy.deepcopy(self)

class PrototypeRegistry:
    def __init__(self) -> None:
        self._prototypes: dict[str, Document] = {}

    def register(self, key: str, proto: Document) -> None:
        self._prototypes[key] = proto

    def create(self, key: str, **overrides) -> Document:
        doc = self._prototypes[key].clone()
        for k, v in overrides.items():
            setattr(doc, k, v)
        return doc

if __name__ == "__main__":
    base = Document("Report", ["Intro", "Data"], {"confidential": True})

    registry = PrototypeRegistry()
    registry.register("report", base)

    quick = registry.create("report", title="Weekly Report")
    quick.body.append("Conclusion")

    print(base.title, base.body)
    print(quick.title, quick.body)
```

Quick glance
- Provide clone() method; decide shallow vs deep.
- Keep a registry for convenient cloning.
- Great when object setup is expensive.
