# == Question
# Find second largest element in array
# == Link
# https://www.codingninjas.com/codestudio/problems/second-largest-element-in-the-array_873375
# == Articles:
# 
# == Explain
# 


def findSecondLargest(arr):
    max_ele, sec_max = float("-inf"),float("-inf")
    for x in arr:
        # in case new max is found, udpate and make older max as second_max
        if x>max_ele:
            sec_max = max_ele
            max_ele = x
        # x > sec but not smaller than max (Also handle duplicates)
        elif x>sec_max and x!=max_ele:
            sec_max = x
    
    return sec_max if sec_max!=float("-inf") else -1