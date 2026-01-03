# Command (Behavioral)

Ref: https://refactoring.guru/design-patterns/command

Overview
- Encapsulates a request as an object, allowing parameterization, queuing, logging, undo/redo.

When to use
- You need undo/redo, logging, macro commands, or queueing.

How to identify
- Command interface with `execute()` (and optional `undo()`), invoker stores commands, receiver performs actions.

Pros
- Decouples invoker from receiver.
- Enables undo/redo and macro commands.

Cons
- Many small classes.

Common confusions
- vs Strategy: Strategy is an interchangeable algorithm; Command represents an action with a receiver and history.

Python example (text editor with undo)
```python
from __future__ import annotations
from abc import ABC, abstractmethod

class Editor:
    def __init__(self) -> None:
        self.text = ""

class Command(ABC):
    def __init__(self, editor: Editor) -> None:
        self.editor = editor
        self._backup = ""

    def save_backup(self) -> None:
        self._backup = self.editor.text

    def undo(self) -> None:
        self.editor.text = self._backup

    @abstractmethod
    def execute(self) -> None: ...

class TypeCommand(Command):
    def __init__(self, editor: Editor, payload: str) -> None:
        super().__init__(editor)
        self.payload = payload

    def execute(self) -> None:
        self.save_backup()
        self.editor.text += self.payload

class Invoker:
    def __init__(self) -> None:
        self._history: list[Command] = []

    def run(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)

    def undo(self) -> None:
        if self._history:
            self._history.pop().undo()

if __name__ == "__main__":
    editor = Editor()
    inv = Invoker()
    inv.run(TypeCommand(editor, "Hello"))
    inv.run(TypeCommand(editor, " World"))
    print(editor.text)
    inv.undo()
    print(editor.text)
```

Quick glance
- Command objects wrap actions; invoker stores/runs them.
- Add undo by saving state inside commands.
