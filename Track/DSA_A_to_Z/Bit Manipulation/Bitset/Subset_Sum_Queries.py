
def subset_sum_queries(arr: list[int], queries: list[int]):
    # create subset sum
    bitset = 1
    for x in arr:
        bitset = (bitset | (bitset<<x))
    
    res = []
    for query in queries:
        res.append((
            query,
            bitset & (1<<query) != 0
        ))
    
    print(res)


arr = [1,2,3,5,10,12,15]
queries = [3, 10, 15, 50]

print(subset_sum_queries(arr, queries))