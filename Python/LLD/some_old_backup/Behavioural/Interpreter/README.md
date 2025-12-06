# Interpreter (Behavioral)

Ref: https://refactoring.guru/design-patterns/interpreter

Overview
- Defines a grammar for a simple language and uses an interpreter to evaluate sentences in the language.
- Represent grammar rules as classes; parse trees evaluate by traversing nodes.

When to use
- You have a simple, well-defined grammar that changes rarely.
- You want to represent and evaluate expressions (filters, queries, rules) in code.

How to identify
- Expression interface with `interpret(context)`; composite tree of terminal and non-terminal expressions.

Pros
- Easy to extend grammar by adding new expression classes.
- Clear mapping between grammar and code.

Cons
- Class explosion for complex grammars.
- Performance can suffer vs. parser generators or compiled evaluators.

Common confusions
- vs Strategy: Interpreter is about evaluating language sentences; Strategy is swapping algorithms.
- vs Visitor: Visitor can traverse expression trees to add new operations; Interpreter focuses on evaluation.

Python example (boolean rule expressions)
```python
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
    # Expression: (A AND B) OR (NOT C)
    expr = Or(And(Literal("A"), Literal("B")), Not(Literal("C")))

    ctx = {"A", "B"}
    print(expr.interpret(ctx))  # True
    ctx = {"A", "C"}
    print(expr.interpret(ctx))  # False
```

Quick glance
- Map grammar rules to classes; build expression trees; call interpret().
