"""
1. Initialization:
- Set num1 and num2 to first two elements.
- Set count1 and count2 to 1.

2. Identification:
- Iterate through array from second element.
    - If matches num1, increment count1.
    - If matches num2, increment count2.
    - If not, decrement count1 and count2. 
    - If either hits 0, update num1 or num2.
        - Here in case, count=0 and you re-assign num1=x make sure (x!=num2)

3. Since 0,1 or 2 majority elements can be present, manually check if count(num1 and num2)>(n//3)
"""


def majorityElement(arr: [int]) -> [int]:
    count1, num1 = 0, float('-inf')
    count2, num2 = 0, float('-inf')

    for x in arr:
        if x == num1:
            count1 += 1
        elif x == num2:
            count2 += 1
        elif count1 == 0: # make sure num2!=x (ALREADY TAKEN CARE ABOVE)
            num1, count1 = x, 1
        elif count2 == 0: # maek sure num1!=x (ALREADY TAKEN CARE ABOVE)
            num2, count2 = x, 1
        else:
            count1 -= 1
            count2 -= 1

    # Count occurrences of num1 and num2
    count1, count2 = 0, 0
    for x in arr:
        if x == num1:
            count1 += 1
        elif x == num2:
            count2 += 1

    # Check if num1 and num2 are majority elements
    req_count = len(arr) // 3
    res = []
    if count1 > req_count:
        res.append(num1)
    if count2 > req_count:
        res.append(num2)

    return res