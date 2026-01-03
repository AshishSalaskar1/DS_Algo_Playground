# Strategy (Behavioral)

Ref: https://refactoring.guru/design-patterns/strategy

Overview
- Define a family of algorithms, encapsulate each, and make them interchangeable at runtime.

When to use
- Swap algorithms based on context (sorting, pricing, routing).

How to identify
- Context holds a Strategy interface reference and delegates algorithm calls.

Pros
- Eliminate conditional chains; open for new algorithms.

Cons
- Many small classes/functions.

Common confusions
- vs State: State changes behavior via transitions; Strategy is selected by client or context.

Python example
```python
from typing import Protocol, Callable

class Strategy(Protocol):
    def __call__(self, data: list[int]) -> list[int]: ...

def sort_asc(data: list[int]) -> list[int]:
    return sorted(data)

def sort_desc(data: list[int]) -> list[int]:
    return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def run(self, data: list[int]) -> list[int]:
        return self.strategy(data)

if __name__ == "__main__":
    ctx = Context(sort_asc)
    print(ctx.run([3,1,2]))
    ctx.strategy = sort_desc
    print(ctx.run([3,1,2]))
```

Quick glance
- Encapsulate algorithms; swap them at runtime.
