"""
PROBLEM: https://leetcode.com/problems/combination-sum-ii/
- Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
- Each number in candidates may only be used once in the combination.
- Note: The solution set must not contain duplicate combinations.

SOLUTION:
- Dont need duplicates and answers also look to be in sorted -> SO SORT ARRAY
- solve(i, target) -> can you make target = target by picking elements from i onwards(including i)
  - you can pick any elements from i -> n
    - in case its > i (check if its duplicate, you need to keep the first one)
    - in case its > target: break since its sorted, if u cant add this means further elements also cant be added
    - add cur_ele to res
    - solve(cur_idx+1, target-arr[cur_idx])
    - pop cur_ele # BACKTRACKING

"""

class Solution:
    def solve(self, i, target, res):
        # print(i,target,res, "=>", target)
        if target == 0:
            self.ans.append(res.copy())
            return 
        
        for next_pick in range(i, len(self.arr)):
            # not the first pickable element nd already seen before (first one you can allow)
            if next_pick > i and self.arr[next_pick] == self.arr[next_pick-1]:
                continue

            # since array is sorted -> if you can pick this, all net elements are greater n cant be picked
            if self.arr[next_pick] > target:
                break

            res.append(self.arr[next_pick])
            self.solve(next_pick+1, target-self.arr[next_pick], res)
            res.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.arr = sorted(candidates)
        self.ans = []
        self.solve(0,target, [])
        # print(self.ans)
        return self.ans

        