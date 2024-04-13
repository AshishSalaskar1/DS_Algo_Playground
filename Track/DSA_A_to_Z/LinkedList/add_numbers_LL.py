"""
INTUITION:
- val1+val2 = res
- keep_val = res%10
- carry_val = res//10

Case 1: Both nums are equal length
[1 -> 2 -> 3]
[4 -> 5 -> 6]
[5 -> 7 -> 9] <- RES

Case 2: Unequal length
- Make sure to count carry also after lists are exhausted
# 7 5 9 4 6
# 8 4
# 5 0 0 5 6 <- RES

Case 3: Carry still remains after all digits are over
- Make sure to count carry also after lists are exhausted
# 5 1 0 6
# 6 7 3 4
# 1 9 3 0 1 <- RES
"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# single while loop
def addTwoNumbers(head1: Node, head2: Node) -> Node:
    res_head = Node(-1)
    res = res_head

    has_carry, carry_num = False, 0

    while head1 or head2:
        val1, val2 = 0, 0

        if head1:
            val1 = head1.data
            head1 = head1.next
        if head2:
            val2 = head2.data
            head2 = head2.next

        csum =  + val1 + val2 + carry_num
        if csum >= 10:
            carry_num = csum// 10
            csum = csum%10
        else:
            carry_num = 0
        
        res.next = Node(csum)
        res = res.next
 
    # carry is stil remaining -> reverse the last 2 digits
    if carry_num != 0:
        res.next = Node(carry_num)

    return res_head.next

def addTwoNumbers(head1: Node, head2: Node) -> Node:
    res_head = Node(-1)
    res = res_head

    has_carry, carry_num = False, 0

    while head1 and head2:
        csum = head1.data + head2.data + carry_num
        if csum >= 10:
            carry_num = csum// 10
            csum = csum%10
        else:
            carry_num = 0
        
        res.next = Node(csum)
        res = res.next


        head1 = head1.next
        head2 = head2.next

    # one is left
    while head1 is not None:
        csum = head1.data + carry_num
        if csum >= 10:
            carry_num = csum// 10
            csum = csum%10
        else:
            carry_num = 0

        res.next = Node(csum)
        res = res.next
        head1 = head1.next

    
    while head2 is not None:
        csum = head2.data + carry_num
        if csum >= 10:
            carry_num = csum// 10
            csum = csum%10
        else:
            carry_num = 0

        res.next = Node(csum)
        res = res.next
        head2 = head2.next

    
    # carry is stil remaining -> reverse the last 2 digits
    if carry_num != 0:
        res.next = Node(carry_num)

    
    return res_head.next
    



 