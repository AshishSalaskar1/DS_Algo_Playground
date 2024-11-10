"""

https://codeforces.com/contest/1732/problem/B

LOGIC:
- You will start swapping when you see first 1->0 (0->1 is fine)
- Once you start flipping, each subsequent mismatch 01 or 10 both will need a flip

"""
import sys
def get_input():
    n = int(sys.stdin.readline())
    cases = []
    
    for _ in range(n):
        sys.stdin.readline()
        cases.append([int(x) for x in sys.stdin.readline().strip()])
    return n, cases

def main():
    N, cases = get_input()
    for arr in cases:
        n = len(arr)
        flip_started = False

        flips = 0
        for i in range(1, n):
            if arr[i-1] != arr[i]:
                if not flip_started:
                    if arr[i-1] == 1:
                        flips += 1
                        flip_started = True
                else:
                    flips += 1

        print(flips)




main()