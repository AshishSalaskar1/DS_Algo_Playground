## Bitset

💡 **IDEA**: 
- In many languages INT is at max 32 or 64 bit at max. 
- So consider each bit as number. 64 63 62 ... 5 4 3 2 1 0. Now in Python int is infinite so you can use it, but in other languages we have separate BITSET
- TC for operations = `N/32` or `N/64` based on the compiler


### 1. Subset Sum Queries
| Doing Subset sum once is easy, but if there any Q queries, you cant build the DP each time

💡 IDEA
- Each bit `i` represents if is subset sum of `i` possible
- 0000000001 - Subset sum of 0 is always possible hence 0th bit is always set

- Now, assume your arr = [2,4] # **SORTED ARRAY ONLY**
- `x` = cur_arr element
1. `x = 2` | bitset = `0000000001`
    - Now, all possible subset sums = x+(previously possible susbset sums = bits set as 1)
    - Ideally, you add
        1. bitset << x(2) = 0000000100
        2. bitset | bitset<<x(2) = 0000000101 ( Here now if you see 0th and 2nd bit is set -> Meaning 0,2 are possible sums)
    - THINK OF THIS AS: `bitset | bitset<<x` => Add `x` to each set bit after `x`.
        - Why this works? WE SORT THE ARRAY -> hence there will be no set bit before `x`
    - OUTPUT: bitset = `0000000101`
2. `x = 4` | bitset = `0000000101`
    - `0000000101` | `0001010000` = `0001010101`

**💡NOTE: WHY MASK MAYBE NEEDED**: 
- Here since we add `x` to every number on left of `x` we dont need a mask
- In some problems, you may want to add to only some bits on left, there you need BITMASK -> THEN OR with BITMASK

**OUTPUT**: 
9876543210
0001010101
- Possible subset sums = 0,2,4,6

3. CHECK IF SUBSET SUM: Just check of `query`th bit is set or not

```py

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

subset_sum_queries(arr, queries)

```