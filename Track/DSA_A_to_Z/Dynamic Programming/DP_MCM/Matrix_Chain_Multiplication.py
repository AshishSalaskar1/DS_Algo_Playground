"""
PROBLEM:
    
4,5,3,2
A = 4x5
B = 5x3
C = 3x2

BEST = A(BC)
- BC will take 5*3*2 operations = 30 (N its size will be 5x2)
- A(4x5) X BC(5x2) = 4*5*2 = 40
Total ops: 40+30 = 70

IMP: cost = cost of multiplication based on dimensions + (cost of multiply each of the )

SOLUTION
idx: 0 1 2 3
ARR: 4,5,3,2
=> Convention: lets assume index(a)=1 such that A=arr[i-1]xarr[i] (i=1) here
- So, index(a)=1, index(b)=2, index(c)=3
- Initially you have i=0, j=n-1 [REMEMBER ITS n-1 -> INCLUSIVE]

- Now try to make all partitions in arr[i:j] (You cant take all in one)
    => `k` is the last element in first partition, `k+1` is first element in second partition
    for k: i -> j: (i,j-1) but since j is already n-1 and python does <n
        
        - You can now split the array into 2 partitions at k
        - cost = multiplying_cost + costs_of_each_partitions
        1. multiplying_cost = arr[i-1]*arr[k]*arr[j]
        2.costs_of_each_partitions = fn(i,k) + fn(k+1,j)

=> multiplying_cost = arr[i-1]*arr[k]*arr[j]
idx: 0 1 2 3
ARR: 4,5,3,2
Example 1:
- i=1,j=3 ==> k=1
- [A(4x5)]x[BC(5x2)] => 4x5x2 = 40
- rows_in_first_matrix_left X cols_in_last_matrix_left X cols_in_last_matrix_right
- arr[i-1] * arr[k] 

Example 1:
- i=1,j=3 ==> k=1
- [A(4x5)]x[BC(5x2)] => 4x5x2 = 40
- rows_in_first_matrix_left X cols_in_last_matrix_left X cols_in_last_matrix_right

GENERAL MCM IDEAS
1. Run some function initially on entire array/partition
   But here init of i,j changes
2. Try all possible partitions in (i,j) and memoize recursively
3. Needs memoization

- There is also some trick to init [i,j] or to pad values
Example
- MCM: You take i=1, since you consider arr[i-1],arr[i] as one MATRIX CORDS
- Stick Cut: [0, *cuts, n] -> Use this so that arr[j+1]-arr[i-1] always gives you length before cutting

"""

from functools import cache
class MCM:
	def __init__(self, arr):
		self.arr = arr

	@cache
	def fn(self, i, j):
		if i == j:
			return 0

		min_ops = float("inf")
		for k in range(i, j):  # i ... j-1
			steps = self.arr[i-1] * self.arr[k] * self.arr[j] + self.fn(i, k) + self.fn(k+1, j)
			min_ops = min(min_ops, steps)
		return min_ops


def matrixMultiplication(arr, n):
	mcm = MCM(arr)
	return mcm.fn(1,n-1)

arr = [4,5,3,2] # 70
print(matrixMultiplication(arr, len(arr)))

arr = [10,15,20,25] # 8000
print(matrixMultiplication(arr, len(arr)))


