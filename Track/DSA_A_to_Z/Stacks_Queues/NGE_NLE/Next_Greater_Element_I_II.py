"""
1. NEXT GREATER ELEMENT - NO CIRCULAR
- Traverse from FIRST <- LAST
- If ele <= stack.top() -> keep on popping
    - Why pop? will those never be NGE of elements on left?
    - No..You need next greater element (first greater element) -> which is ele [you will never reach nums in stack < ele]
- If stack.empty() -> -1 (no NGE), else NGE=stack.pop() [this is the first ele in stack > ele]
- stack.push(ele) -> cur ele will always be greater that stack.top()

Example:
5,  7, 1,  7,  6, 0
7, -1, 7, -1, -1, -1

2. NEXT GREATER ELEMENT - CIRCULAR
- Concat arrays twice (arr, arr) and pick NGE for first [0-n] chars
- Instead of manually concating arrays -> use mod operations


Examples:
5, 7,1, 7, 6,0
7,-1,7,-1,7,5

"""

from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    n = len(arr)
    res = [-1 for _ in range(n)]
    st = []

    for i in reversed(range(n)):
        x = arr[i]
        # remove all elements > cur
        while len(st) != 0 and st[-1] <= x:
            st.pop()

        if len(st) == 0: # no NGE
            res[i] = -1
        else: # NGE = stack.top()
            res[i] = st[-1]
        st.append(x) # add cur element

    return res

def nextGreaterElementCircular(arr: List[int], n: int) -> List[int]:
    n = len(arr)
    res = [-1 for _ in range(n)]
    st = []

    for i in reversed(range(2*n)):
        x = arr[i%n]

        while len(st) != 0 and st[-1] <= x:
            st.pop()

        if i<n:
            if len(st) == 0:
                res[i] = -1
            else:
                res[i] = st[-1]

        # keep on adding curr
        st.append(x)

    return res


arr = [5,  7, 1,  7,  6, 0]
# [7, -1, 7, -1, -1, -1]
print(nextGreaterElement(arr, len(arr)))

arr = [5,  7, 1,  7,  6, 0]
# [7, -1, 7, -1, -1, -1]
print(nextGreaterElementCircular(arr, len(arr)))

