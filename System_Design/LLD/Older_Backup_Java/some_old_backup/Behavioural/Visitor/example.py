from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_number(self, e: "Number") -> None: ...

    @abstractmethod
    def visit_add(self, e: "Add") -> None: ...

class Expr(ABC):
    @abstractmethod
    def accept(self, v: Visitor) -> None: ...

class Number(Expr):
    def __init__(self, value: int) -> None:
        self.value = value

    def accept(self, v: Visitor) -> None:
        v.visit_number(self)

class Add(Expr):
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left = left
        self.right = right

    def accept(self, v: Visitor) -> None:
        v.visit_add(self)

class Printer(Visitor):
    def visit_number(self, e: Number) -> None:
        print(e.value, end="")

    def visit_add(self, e: Add) -> None:
        e.left.accept(self)
        print(" + ", end="")
        e.right.accept(self)

if __name__ == "__main__":
    expr = Add(Number(1), Add(Number(2), Number(3)))
    Printer().visit_add(expr)
