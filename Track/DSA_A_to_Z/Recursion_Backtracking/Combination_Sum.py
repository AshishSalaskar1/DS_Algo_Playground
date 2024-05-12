"""
Solution: https://takeuforward.org/data-structure/combination-sum-1/

"""
class Solution:
    def findCombination(self, ind: int, target: int):
        if ind == len(self.candidates):
            if target == 0:
                self.ans.append(self.ds[:])
            return

        # PICK -> if possible + BACKTRACK PICKED ONE FROM PICKED_ELEMENTS
        if self.candidates[ind] <= target: # you can pick the ele
            self.ds.append(self.candidates[ind])
            self.findCombination(ind, target - self.candidates[ind]) # you can pick same again
            self.ds.pop()
        # DONT PICK
        self.findCombination(ind + 1, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.ds = []
        self.candidates = candidates
        self.target = target
       
        self.findCombination(0, target)
        return self.ans
        