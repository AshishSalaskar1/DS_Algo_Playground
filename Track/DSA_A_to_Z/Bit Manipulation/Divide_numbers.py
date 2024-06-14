"""
Problem: https://leetcode.com/problems/divide-two-integers/
- Divide 2 numbers without using multiplication, division and modolus operator
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1

        sign = 1
        if (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0):
            sign = -1
        
        num, den = abs(dividend), abs(divisor)
        quotient = 0

        while num >= den:
            power = 0
            while num >= (den<<(power+1)):
                power += 1
            
            quotient += 1<<power
            num -= (den<<power)

        if quotient == (1<<31) and sign==1:
            return (1<<31)-1
        elif quotient == (1<<31) and sign==-1:
            return -1*(1<<31)
        
        return sign*quotient
    