"""
=> LC Link (only evaluation): This deals with evaluate to True only

=> Problem Statement: Given an expression, A, with operands and operators (OR, AND, XOR)
- In how many ways can you evaluate the expression to be true, by grouping it in different ways?
- In 1 operation you do one operand-operator-operand operation, but the order can be anything but atlast you need one answer which is True
- Operands are only true and false.
    
=> SOLUTION
- We know that the expression is always in format: x1[OP]x2[OP]x3[OP] (an operator is sourrounded by 2 operands at its both sides)
- There are no brackets or any other grouping, its pure operand-operator-operand format 

=> INTUITION
- We need to calculat the num_ways to get True (all possible ways/combinations)
- So let your fn(start, end, needTrue)
    1. needTrue=True, returns number of possible True answers
    2. needTrue=False, returns number of possible False answers
    
=> BASE CASES
- if i>j = return 0 (exceeds bounds)
- if i==j = only single operand is left (1 if its True and needTrue=True, or False and needTrue=False)
    
=> SPLITTING
- iterate k: i+1 -> j-1 (increments of 2) -> You want to ITERATE ONLY ON OPERATORS
    - at each point you can split it into 2 subproblems
      1. (i,k-1)
      2. (k+1, j)

=> POSSIBLE WAYS 
- Lets say you have [expr1][OPERATOR][expr2]
- leftT, leftF: number of times the left expression got reduced to True and False 
- rigtT, rightF: number of times the right expression got reduced to True and False 

1. AND
- True: only when both are True, False: when either or both are False
- Ways True: leftT*rightT
- Ways False: leftF*rightT + leftT*rightF + leftF*rightF (either False, both False)

2. OR
- True: if either or both are True, False: only if both are False
- Ways True: leftT*rightT + leftF*rightT + leftT*rightF
- Ways False: leftF*rightF

3. XOR
- True: only if 1 is True, False: When both are same (either True or False)
- Ways True: leftT*rightF + leftF*rightT
- Ways False: leftT*rightT + leftF*rightF
    

"""
class Solution:
    def fn(self, i: int, j:int, needTrue:bool) -> int:
        if i>j:
            return 0
        if i==j:
            if needTrue: # return count of T|F -> which is 1 if its T|F
                return int(self.expr[i] == "T")
            else:
                return int(self.expr[i] == "F")

        ways = 0
        for k in range(i+1, j, 2): # j-1 but python < END | 2 because format is x1[op]x2[op]x3[op]x4[op]
            op = self.expr[k]
            leftT = self.fn(i, k-1, True)
            leftF = self.fn(i, k-1, False)
            rightT = self.fn(k+1,j, True)
            rightF = self.fn(k+1,j, False)

            if op == "&":
                if needTrue: # you need to make AND result as True
                    ways += leftT*rightT
                else: # you need to make AND result as False
                    ways += (leftF*rightF) + (leftF*rightT) + (leftT*rightF)
            elif op == "|":
                if needTrue: # you need to make OR result as True
                    ways += (leftT*rightT) + (leftF*rightT) + (leftT*rightF)
                else: # you need to make OR result as False
                   ways += (leftF*rightF)
            elif op == "^": # A^B = True if only either of A or B is True else Fase if both are true or false
                if needTrue:
                    ways += (leftF*rightT) + (leftT*rightF)
                else:
                    ways += (leftF*rightF) + (leftT*rightT)

        return ways

    def boolean_expressions(self, expr):
        self.expr = expr
        i,j = 0, len(expr)-1
        return self.fn(i,j,needTrue=True)

sol = Solution()

expression = "T|T&F" # 1
print(sol.boolean_expressions(expression))

expression = "F|T^F" #2
print(sol.boolean_expressions(expression))
