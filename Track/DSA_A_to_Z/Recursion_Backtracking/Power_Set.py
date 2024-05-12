class Solution:
    def solve(self, p, up):
        if len(up) == 0:
            self.res.append(p)
            return
        
        # remove first unprocessed element from unprocessed
        up_ele = up[0]
        up = up[1:]

        # you have two options 1) pick up_ele 2) dont pick
        # in both cases however its removed from up
        self.solve([*p,up_ele], up)
        self.solve(p, up)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.solve([],nums)
        print(self.res)
        return list(self.res)
        