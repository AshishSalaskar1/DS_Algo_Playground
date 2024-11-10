"""
Problem: https://codeforces.com/problemset/problem/71/A
"""

import sys


def get_input():
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]

    return n,words


def main():
    n, words = get_input()

    for word in words:
        if len(word)>10:
            res = word[0] + str(len(word)-2) + word[-1] 
            print(res)
        else:
            print(word)

main()