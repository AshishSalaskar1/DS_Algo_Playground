"""
You are given the arrival and leaving times of n customers in a restaurant.
What was the maximum number of customers in the restaurant at any time?

Example

Input:
3
5 8
2 4
3 9

Output: 2
"""


import sys

# decorator to read input from file for test cases
# def read_from_file(get_input_fn):
#     def wrapper():
#         with open('/Users/a0s13fj/Desktop/DSA/input.txt', 'r') as f:
#             sys.stdin = f
#             return get_input_fn()

#     return wrapper

# @read_from_file
def get_input():
    n = int(sys.stdin.readline())
    intervals = []
    for _ in range(n):
        start, end = list(map(int, sys.stdin.readline().split()))
        intervals.append((start, end))

    return n, intervals

def main():
    n, intervals = get_input()
    events = []
    for st,end in intervals:
        events.append((st,1))
        events.append((end,-1))

    events = sorted(events)
    max_customers = 0
    n_customers = 0

    for i in range(len(events)):
        n_customers += events[i][1]
        max_customers = max(max_customers, n_customers)

    print(max_customers)
main()
