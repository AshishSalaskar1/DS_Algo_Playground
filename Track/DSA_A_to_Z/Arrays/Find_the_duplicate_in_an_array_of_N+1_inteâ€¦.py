from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    n = len(arr)
    
    i = 0
    for i in range(n):
        # print(i)
        # already in place
        if arr[i] == (i+1):
            continue
        
        while arr[i] != (i+1):
            correct_idx = arr[i]-1
            cur_index = i
            # check if correct index is already in place
            if arr[correct_idx] == arr[cur_index]:
                return arr[cur_index]
            # put it in place
            arr[cur_index], arr[correct_idx] = arr[correct_idx],arr[cur_index]
            
    return