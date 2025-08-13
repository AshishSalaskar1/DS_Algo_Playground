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
