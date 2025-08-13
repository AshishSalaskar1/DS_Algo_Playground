# State (Behavioral)

Ref: https://refactoring.guru/design-patterns/state

Overview
- Allows an object to alter its behavior when its internal state changes; it appears to change its class.

When to use
- Complex conditional logic based on state; transitions between well-defined states.

How to identify
- A context delegates work to a state object that can switch the context's current state.

Pros
- Organizes state-specific behavior into separate classes.
- Eliminates large conditional statements.

Cons
- More classes; can be overkill for simple logic.

Common confusions
- vs Strategy: State transitions are part of the pattern; Strategy is chosen by the client and doesn’t change context state.

Python example (player)
```python
from __future__ import annotations
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def play(self, ctx: "Player"): ...

class Playing(State):
    def play(self, ctx: "Player"):
        print("Already playing; pausing")
        ctx.state = Paused()

class Paused(State):
    def play(self, ctx: "Player"):
        print("Resuming")
        ctx.state = Playing()

class Player:
    def __init__(self) -> None:
        self.state: State = Paused()

    def click_play(self) -> None:
        self.state.play(self)

if __name__ == "__main__":
    p = Player()
    p.click_play()
    p.click_play()
```

Quick glance
- Context holds current State; calls delegate and transition.
