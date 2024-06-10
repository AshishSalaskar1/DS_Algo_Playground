"""
Find XOR of numbers in range (L,R) => L^.......^R

LOGIC - Rules
=> [XOR from 1 -> N]
- If N%4==1 -> XOR(1,N) = 1
- If N%4==2 -> XOR(1,N) = N+1
- If N%4==3 -> XOR(1,N) = 0
- Else, XOR(1,N) = N

=> [NOW XOR(L,R)]
=> XOR(L->R) = XOR(1->L-1) ^ XOR(1->R)

Why XOR(1->L-1) and not L?
XOR(4,6) => You need 4^5^6
- XOR(4,6) = XOR(1,3) ^ XOR(1,6)
                     = (1^2^3) ^ (1^2^3^4^5^6)
                     = (4^5^6) ====> [1,2,3 appear twice so get cancelled, and 4,5,6 appear once]
"""


def XOR_1_to_n(n):
    if n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    elif n%4 == 3:
        return 0
    return n

def XOR_range(l,r):
    return XOR_1_to_n(l-1) ^ XOR_1_to_n(r)

def test(n):
    for i in range(1,n+1):
        res = 0
        for j in range(1,i+1):
            res ^= j
        print(f"XOR(1,{j}) => {res}")

test(20)

"""
=> XOR DRY RUNS
XOR(1,1) => 1
XOR(1,2) => 3
XOR(1,3) => 0
XOR(1,4) => 4
XOR(1,5) => 1
XOR(1,6) => 7
XOR(1,7) => 0
XOR(1,8) => 8
XOR(1,9) => 1
XOR(1,10) => 11
XOR(1,11) => 0
XOR(1,12) => 12
XOR(1,13) => 1
XOR(1,14) => 15
XOR(1,15) => 0
XOR(1,16) => 16
XOR(1,17) => 1
XOR(1,18) => 19
XOR(1,19) => 0
XOR(1,20) => 20
"""
