"""
Algo
1. Choose a ele and make count = 1
2. Iterate the array x
    - if x == choosen_ele -> count += 1 
    - else count -= 1 [ele is different]
    - if count=0, reset ele_chosen and the count
3. Here maj_ele is gauranteed hence res=maj_ele
   Else, count if maj_ele occurs more than n/2 times

Count Logic: The maj_ele occurs more than n/2 times,
    so there are n-(n/2) elements which are different.
    Hence, count for the maj_ele can never become 0 (at max it can be 1)
"""

def majorityElement(arr: [int]) -> int:
    maj_count = 1
    maj_ele = arr[0]

    for x in arr[1:]:
        if x == maj_ele:
            maj_count += 1
        else:
            maj_count -= 1

        if maj_count == 0:
            maj_count = 1
            maj_ele = x


    return maj_ele