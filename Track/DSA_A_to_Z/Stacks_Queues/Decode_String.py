"""
PROBLEM: https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Input: s = "10[abc]"
Output: "abcabcabcabcabcabcabcabcabcabc"
"""

class Solution:
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

    def decodeStringVerbose(self, arr: str) -> str:
        n = len(arr)
        res = ""
        stack = []

        for x in arr:
            if x!="]":
                stack.append(x)
            else: # you encountered a ]

                # find all the chars string
                string = ""
                while stack[-1] != "[":
                    ch = stack.pop()
                    string = ch+string

                stack.pop() # pop [

                # find count - it can be more than 1 digit
                count = ""
                while len(stack)>0 and stack[-1].isdigit():
                    count = stack.pop()+count

                stack.append(string*int(count))
        
        return "".join(stack)


            




            

            
        