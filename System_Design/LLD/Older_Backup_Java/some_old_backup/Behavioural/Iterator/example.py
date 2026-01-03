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
