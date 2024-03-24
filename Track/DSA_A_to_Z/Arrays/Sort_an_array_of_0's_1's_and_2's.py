from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
    zero_ptr = 0
    two_ptr = n-1


    cur_ptr = 0
    # IMP TO REMEMBER  CUR_PTR<TWO_PTR
    while cur_ptr <= two_ptr:
        if arr[cur_ptr] == 0:
            arr[cur_ptr], arr[zero_ptr] = arr[zero_ptr], arr[cur_ptr]
            cur_ptr += 1
            zero_ptr += 1
        elif arr[cur_ptr] == 2:
            arr[cur_ptr], arr[two_ptr] = arr[two_ptr], arr[cur_ptr]
            # u dont increment cur_ptr, because after swap cur_ptr can be either 0 or 1
            # in zero_ptr we are always sure that zer
            two_ptr -= 1
        else:
            cur_ptr += 1 
        # print(arr)
    return arr