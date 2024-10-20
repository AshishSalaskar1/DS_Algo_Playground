"""
PROBLEM: https://leetcode.com/problems/parsing-a-boolean-expression
SOLUTION:
- Use Stacks 

INTUITION:
- If you have any operator or T\F, go on pushing it in the stack
- When you see any ), pop all elements till u see another opening bracket - (
- After this the next ele you pop will be the operator (After you pop the opening bracket)
- Calculate operation on the all the elements between ( and ) which you just popped
- Add answer back to the stack

EXAMPLE 1: &(|(f))
st = [&, (, |, (, False]
=> i=5 -> )
pop_elem = False, op = | => |False => False 
st = [&, (, False]

=> i=6 => )
pop_elems = False, op=&, &False = False
st = [False]

EXAMPLE 2: !(&(f,t))
st = [!,(,&,(,False,True]
=> i=8, )
pop_elems = [True, False] op=&, True&False =  False
st = [!,(,False]
=> i=9, )
pop_elems = [False], op=! , NOT False = True
st = [True]

"""
class Solution:
    def parseBoolExpr(self, expr: str) -> bool:
        n = len(expr)
        st = []

        i = 0
        
        while i<n:
            # print(i, expr[i], st)
            if expr[i] in set(list("(!&|tf")):
                if expr[i] in "tf": # in case its T\F, put actual True, False values
                    st.append(True if expr[i] == "t" else False)
                else:
                    st.append(expr[i])
            elif expr[i] == ",": # ignore commas
                i += 1
                continue
            elif expr[i] == ")":
                eles = []
                while st and st[-1] != "(": # pop all elements until you see opening brace - (
                    eles.append(st.pop())
                
                st.pop() # remove (
                op = st.pop() # remove operator

                res = eles[0]
                for x in eles[1:]:
                    if op == "|":
                        res |= x
                    elif op == "&":
                        res &= x
                
                if op == "!":
                    res = not res
                
                st.append(res) # append back the res

            i += 1

        return st[-1]


                

        