"""
Problem: Successful Pairs of Spells and Potions
- https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=study-plan-v2&envId=leetcode-75

- SPELLS, POTIONS, SUCCESS
- For each potion, return the num of spells when its paired with gives product > sucesss

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

SOLUTION:
- SORT POTIONS
- For each spell, find lowest index item in potions st spell*potion >= success
    - num elements = len(potions)-lowest_index [Since its sorted, all potions after lowest_idx will also be valid pairs]
"""


class Solution: 
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ns, np = len(spells), len(potions)

        potions = sorted(potions)
        # print(potions)
        res = []
        for x in spells:
            if x*potions[-1] < success:
                res.append(0)
                continue

            lo,hi = 0, np-1
            min_index = -1
            while lo<=hi:
                mid = lo + (hi-lo)//2
                midval = potions[mid]*x

                if midval >= success: # we need least index which gives success
                    min_index = mid
                    hi = mid-1
                else:
                    lo = mid+1

            res.append(np-min_index)
        
        return res


"""
T = 7
1 ,2 ,3 ,4 ,5
8 ,4 ,3 ,2, 2
"""