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
