"""

Given an array of of length N which supposed to contain numbers 1 to N, 
1. There is one number which is repeated twice 
2. One number which is missed 
Find the REPEATED and MISSING number

Example:
arr = [6,4,3,5,5,1] # repeated: 5, missing: 2
expected_arr = [1,2,3,4,5,6]

sum_n = (n*(n+1))/2
sum_n2 =  (n*(n+1)*(2n+1))/6
sum_arr = sum(arr)

X: repeating number, Y: missing number
sum_arr - sum_n = X-Y (from sum_arr only repeating will be left)
sum_arr2 - sum_n2 = X^2 - Y^2 = (x-y)(x+y) [same logic as above]
X+Y = (sum_arr2-sum_n2) / (sum_arr-sum_n)

You have X+Y and X-Y
(X+Y) + (X-Y) = X+Y+X-Y = 2X
==> X = ((X+Y)+(X-Y)) // 2 || REPEATED NUMBER
(X+Y) - (X-Y) = X+Y-X+Y = 2Y 
==> Y = ((X+Y)-(X-Y)) // 2 || MISSING NUMBER
"""

def get_missing_repeated_num(arr):
    n = len(arr)
    
    sum_n = (n*(n+1))//2
    sum_n2 =  (n*(n+1)*((2*n)+1))//6
    sum_arr = sum(arr)
    sum_arr2 = sum([x*x for x in arr])
    
    x_minus_y = sum_arr - sum_n
    x_plus_y = (sum_arr2-sum_n2) // x_minus_y

    repeated_num = (x_plus_y+x_minus_y)//2
    missing_num = (x_plus_y-x_minus_y)//2
    # missing_num = repeated_num - x_minus_y
    
    return repeated_num, missing_num
    
arr = [6,4,3,5,5,1]
repeated_num, missing_num = get_missing_repeated_num(arr)

print(repeated_num, missing_num)



    
# print(xor)
# print(xor --> mivi roamler which is that we can then )
# print(xor --> poetry --> )