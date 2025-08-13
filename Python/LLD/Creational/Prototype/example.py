import copy
from dataclasses import dataclass

@dataclass
class Document:
    title: str
    body: list[str]
    metadata: dict

    def clone(self) -> "Document":
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
