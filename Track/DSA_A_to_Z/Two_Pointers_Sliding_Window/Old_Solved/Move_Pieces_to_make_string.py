"""
Problem: https://leetcode.com/problems/move-pieces-to-obtain-a-string/

Solution: https://leetcode.com/problems/move-pieces-to-obtain-a-string/solutions/2261229/faster-than-100-00-o-n-java-and-c


IDEA:
- You need to have same OPS in same order (ignoring whitespaces since you cant jump across, just move to and fro)


"""
class Solution:
    def canChange(self, src: str, dest: str) -> bool:
        sq = [(idx,val) for idx,val in enumerate(src) if val!="_"]
        dq = [(idx,val) for idx,val in enumerate(dest) if val!="_"]

        if len(sq) != len(dq):
            return False

        print(sq, dq)
        for i in range(len(sq)):
            if sq[i][1] != dq[i][1]:
                return False
            
            if dq[i][1] == "L":  # both are Ls
                if sq[i][0] < dq[i][0]: # in src -> you can only move left
                    return False
            else:  # both are Rs
                if sq[i][0] > dq[i][0]: # -> in src you can only move right
                    return False
        
        return True






        

        