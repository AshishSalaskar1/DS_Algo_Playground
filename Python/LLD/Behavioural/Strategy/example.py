from typing import Protocol

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
