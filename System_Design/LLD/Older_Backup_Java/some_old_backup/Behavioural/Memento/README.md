# Memento (Behavioral)

Ref: https://refactoring.guru/design-patterns/memento

Overview
- Captures and externalizes an object's internal state so it can be restored later, without exposing its internals.

When to use
- You need undo/rollback in a safe way.

How to identify
- Originator creates mementos; Caretaker keeps them; Memento stores state.

Pros
- Encapsulates state snapshots cleanly.

Cons
- Memory usage if snapshots are large/frequent.

Common confusions
- vs Command undo: Memento stores state; Command typically stores inverse operations or state backups.

Python example
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class EditorMemento:
    text: str

class Editor:
    def __init__(self) -> None:
        self.text = ""

    def create_memento(self) -> EditorMemento:
        return EditorMemento(self.text)

    def restore(self, m: EditorMemento) -> None:
        self.text = m.text

class History:
    def __init__(self) -> None:
        self._stack: list[EditorMemento] = []

    def push(self, m: EditorMemento) -> None:
        self._stack.append(m)

    def pop(self) -> EditorMemento | None:
        return self._stack.pop() if self._stack else None

if __name__ == "__main__":
    editor = Editor()
    history = History()

    editor.text = "Hello"
    history.push(editor.create_memento())
    editor.text = "Hello World"

    m = history.pop()
    if m:
        editor.restore(m)
    print(editor.text)
```

Quick glance
- Save/restore snapshots without exposing internals.
