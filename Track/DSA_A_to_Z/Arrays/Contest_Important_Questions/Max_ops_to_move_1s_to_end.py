"""
PROBLEM:https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

"1001101" - 4
"00111" - 0
"10011010" - 8

Optimized Solutions
1. https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/solutions/5508962/greedy

ONE-PASS on SOLUTION 1:
- Whenever u see [1,0], that means you will shift all 1s before 0 to next island
    - res += ones_seen_till(i)
    - This accounts the island formation also, you are `i` means all the 1-islands have been grouped already
    - This is same as calculating CARRY and then adding it to res

SOLUTION 1:
1. set `end` to last 0 (first non-1 from left<-right)
2. Also, have a arr to store next closest 1 on right side (eliminate TLE)
3. Consider, you are at a 1
    - You need to take k steps to reach from here to next 1 island
    - k = cur_island_ones + len(all previously carried islands)
    - res += cur_island_size + carry (you will take cur_size+any_prev_carries) steps to move this island and join in next
      carry = cur_island_size + carry (include this island_size in carry to use in next)
4. If there is no next 1-Island to move to => BREAK and return res
    - You dont need to worry abt carry. Why? In last step you accounted steps to reach next 1-island (which is end in this case)

DRY RUN:
[1]00[11]0[1]0
- 1st island: res=0+ island_size(1) + carry(0)=1,   carry=0+1=1
- 2nd island: res=1+ island_size(2) + carry(1)=4,   carry=1+2=3
- 3rd island: res=4+ island_size(1) + carry(3)=8,   carry=3+1=4 
RES = 8
"""

class Solution:
    def maxOperations(self, s: str) -> int:
        arr = [int(x) for x in list(s)]
        res, one_count = 0, 0
        for i in range(len(arr)-1):
            if arr[i] == 1: # adding first, since you looking ahead for 0: [1]->0 and not 1->[0]
                one_count += 1

            if arr[i]==1 and arr[i+1]==0:
                res += one_count

        return res



    def maxOperationsLong(self, s: str) -> int:
        arr = [int(x) for x in list(s)]
        n = len(arr)

        next_one = [-1]*n
        last_seen = -1
        
        for i in reversed(range(n)):
            if arr[i] == 1:
                next_one[i] = last_seen
                last_seen = i
        
        
        res, carry, end = 0, 0, 0
        end = n-1
        
        # get the last zero index (1 in last are already in place)
        while end>=0 and arr[end] == 1:
            end -= 1
        if end < 0:
            return 0

        # print("end: ", end)

        while i<=end:
            if arr[i] == 0:
                i += 1
            else: # one found
                cur_island_size = 1
                while i+1<=end and arr[i+1] == 1:
                    i += 1
                    cur_island_size += 1

                res += cur_island_size + carry
                carry = cur_island_size + carry
                
                if next_one[i] == -1: # THIS IS THE LAST ONE
                    break
                i = next_one[i]
        
        return res 