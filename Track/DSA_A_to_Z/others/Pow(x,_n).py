"""
ODD
2^5 = 2 * 2^4

EVEN
2^4 = (2^2)^2
2^8 = (2^2)^4
2^16 = (2^2)^8

If its ODD then u defintely know when u do res=res*base the power now becomes even

Algo:
# handle negative power
X^-n = (1/X)^n
if power is -ve:
    n = -1*power
    base = 1/base
    

res = 1
while power>0:
    if power is odd:
        res = res*base and n--
    # now power is even for sure
    -> square base and n//2
"""


def power(base, n):
    # handle negative 
    if n < 0:
        base = 1 / base
        n = -n
        
    res = 1  # Initialize the result variable
    while n > 0:
        if n % 2 == 1:  # If n is odd
            res *= base
        base *= base  # Square the base
        n //= 2  # Integer division by 2
    return res
    


print(power(2,10))
# print(power(10,3))
# print(power(10,4))
# print(power(3.7,3)) # 50.653000000000006
# print(power(13.1655,2)) # 173.330390