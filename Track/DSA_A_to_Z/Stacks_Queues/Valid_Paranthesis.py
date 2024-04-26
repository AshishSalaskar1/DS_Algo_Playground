class Solution:
    def isValid(self, arr: str) -> bool:
        stack = []
        op_close_map = {"}":"{", ")":"(", "]":"["}

        for x in arr:
            if x in {"(","[","{"}:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if op_close_map[x] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(x)

        return len(stack) == 0    