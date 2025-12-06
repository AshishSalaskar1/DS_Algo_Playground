import sys


def get_input():
    n = int(sys.stdin.readline())
    cases = []

    for _ in range(n):
        cases.append(int(sys.stdin.readline().strip()))

    return n, cases


def main():
    N, cases = get_input()

    for n in cases:
        lo, hi = 1, (3 * n) - 1

        while lo < hi:
            print(lo, hi)
            lo += 2
            hi -= 3


main()
