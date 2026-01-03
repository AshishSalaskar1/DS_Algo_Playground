from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Set

class Expr(ABC):
    @abstractmethod
    def interpret(self, ctx: Set[str]) -> bool: ...

class Literal(Expr):
    def __init__(self, name: str) -> None:
        self.name = name

    def interpret(self, ctx: Set[str]) -> bool:
        return self.name in ctx

class And(Expr):
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left = left
        self.right = right

    def interpret(self, ctx: Set[str]) -> bool:
        return self.left.interpret(ctx) and self.right.interpret(ctx)

class Or(Expr):
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left = left
        self.right = right

    def interpret(self, ctx: Set[str]) -> bool:
        return self.left.interpret(ctx) or self.right.interpret(ctx)

class Not(Expr):
    def __init__(self, expr: Expr) -> None:
        self.expr = expr

    def interpret(self, ctx: Set[str]) -> bool:
        return not self.expr.interpret(ctx)

if __name__ == "__main__":
    expr = Or(And(Literal("A"), Literal("B")), Not(Literal("C")))
    ctx = {"A", "B"}
    print(expr.interpret(ctx))
    ctx = {"A", "C"}
    print(expr.interpret(ctx))
