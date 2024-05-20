"""
SOLUTION: UNPROCESSED-PROCESED LOGIC
("23", "a") => 2 (a,b,c) -> ("3", "a"),("3", "b"),("3", "c")
("3", "a") => 3 (d, e, f) -> ("", "ad"), ("", "ae"), ("", "af")

"""
class Solution:
    
    def solve(self, up: str, p: str) -> None:
        if up == "":
            self.res.add(p)
            return
        
        cur_digit = up[0] # first digit in unprocessed string is popped and used
        up = up[1:]

        for ch in self.mapping[cur_digit]:
            self.solve(up, p+ch) # you can only add after already processed one
        
        return 


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        self.mapping = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz")
        }

        self.res = set()
        self.solve(digits, "") # initially you string is unprocessed and nothing is processed
        return list(self.res)
    
