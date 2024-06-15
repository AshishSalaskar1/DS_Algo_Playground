from collections import OrderedDict

class Solution:
    def romanToInt(self, s: str) -> int:
        ops = OrderedDict({
           "I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000 
        })

        st = []

        for ch in s:
            if len(st) != 0 and ops[ch] > st[-1]:  # IX, CM case
                st[-1] *= -1

            st.append(ops[ch])
        
        return sum(st)

    def intToRoman(self, num: int) -> str:
        # Define the mappings of integer values to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ''
        i = 0
        # Construct the Roman numeral
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

# Testing the functions
sol = Solution()
print(sol.romanToInt("MMMDXLIX"))  # Output: 3549
print(sol.intToRoman(3549))        # Output: MMMDXLIX
print(sol.romanToInt("MMXXI"))     # Output: 2021
print(sol.intToRoman(2021))        # Output: MMXXI
