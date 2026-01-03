# Iterator (Behavioral)

Ref: https://refactoring.guru/design-patterns/iterator

Overview
- Provides a way to access elements of a collection without exposing its underlying representation.

When to use
- You need multiple traversal algorithms, or a uniform interface for traversal.

How to identify
- Iterator object with `__iter__` and `__next__` in Python; collection returns an iterator.

Pros
- Encapsulates traversal logic; multiple iterators can traverse independently.

Cons
- Adds extra objects and complexity for simple cases.

Common confusions
- vs Generator: Generators are a Pythonic way to implement iterators; the pattern is the general idea.

Python example (custom range)
```python
class MyRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

if __name__ == "__main__":
    for x in MyRange(3, 6):
        print(x)
```

Quick glance
- Hide collection details; expose `__iter__`.
- Generators often implement this neatly in Python.
