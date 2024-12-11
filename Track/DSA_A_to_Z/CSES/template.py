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
    print(data)
    n, q = data[0], data[1]

    nodes = list(map(int, sys.stdin.readline().split()))
    queries = []

    for _ in range(q):
        queries.append(list(map(int, sys.stdin.readline().split())))

    return n,q,nodes, queries

print(get_input())
# sys.stdout.write("\n".join(map(str, results)) + "\n")