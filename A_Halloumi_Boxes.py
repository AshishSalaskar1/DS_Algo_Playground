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


main()