import sys

# decorator to read input from file for test cases
def read_from_file(get_input_fn):
    def wrapper():
        with open('D://Coding/Github/DS_Algo_Playground/Track/DSA_A_to_Z/CSES/input.txt', 'r') as f:
            sys.stdin = f
            return get_input_fn()
    
    return wrapper

@read_from_file
def get_input():
    data = list(map(int, sys.stdin.readline().split()))
    n, target = data[0], data[1]

    coins = list(map(int, sys.stdin.readline().split()))


n, target, coins = get_input()
print(n, target, coins)

dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(target+1):
        if i==0 or j==0:
            dp[i][j] = 1