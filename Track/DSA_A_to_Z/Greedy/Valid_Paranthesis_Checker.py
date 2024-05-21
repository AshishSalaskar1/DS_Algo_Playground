class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        # L -> R : You replace * with ( in case needed
        balance = 0 # balance of opening braces
        for ch in s:
            if ch == ")":
                balance -= 1
            else: # ( or *
                balance += 1
            
            if balance < 0: # there are less than needed (+* before your )
                return False 
        
        # if balance > 0, means there were more ( + * then needed. Try to replace * with )
        if balance == 0: # you can perfectly balance in case *->()
            return True

        # l <- R : You replace * with ) in case needed
        balance = 0
        for ch in s[::-1]:
            if ch == "(":
                balance -= 1
            else: # ) or *
                balance += 1
            
            if balance < 0: # there are less than needed (+* before your )
                return False 

        return True
        