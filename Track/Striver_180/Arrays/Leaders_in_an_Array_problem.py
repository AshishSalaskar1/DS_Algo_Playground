from typing import *

def superiorElements(arr : List[int]) -> List[int]:
    superior = []

    max_right = float("-inf")

    for i in reversed(range(len(arr))):
        x = arr[i]
        if x>max_right:
            superior.append(x)
        
        max_right = max(x, max_right)
        
    return superior