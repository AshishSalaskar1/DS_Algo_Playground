'''

INTUITION: Same as merge two sorted arrays
1. Set head to either one of the heads of the LL
2. While (you exhaust one LL): pick the smallest of two
3. You might exhaust one but leave another

    Following is the linked list node structure:
    class Node:
        def __init__(self, data):
        self.data = data
        self.next = None
'''

# 1 -> 5-> 7->8
# 2 -> 3 -> 4 


def sortTwoLists(first, second):
    new_head = None
    cur_ptr = new_head

    # set head to smallest head
    if first.data <= second.data:
        new_head = first
        first = first.next
    else:
        new_head = second
        second = second.next
    
    cur_ptr = new_head

    while first and second:
        if first.data <= second.data:
            cur_ptr.next = first
            cur_ptr = cur_ptr.next
            first = first.next
        else:
            cur_ptr.next = second
            cur_ptr = cur_ptr.next
            second = second.next
        
    # one of this might be left
    if first is None or first.next is None:
        while second:
            cur_ptr.next = second
            cur_ptr = cur_ptr.next
            second = second.next
    
    if second is None or second.next is None:
        while first:
            cur_ptr.next = first
            cur_ptr = cur_ptr.next
            first = first.next
        
    return new_head


# IN-PLACE and faster
def sortTwoLists(first, second):
    if first is None:
        return second

    if second is None:
        return first
    
    if first.data <= second.data:
        sptr,lptr = first, second
    else:
        sptr, lptr = second, first

    # this is needed to return
    res = sptr

    while sptr is not None and lptr is not None:
        # point one point behind sptr
        temp = None

        # increment sptr untill its greater than lptr (STABLE)
        while sptr and sptr.data <= lptr.data:
            temp = sptr
            sptr = sptr.next
        
        # point last node in smaller LL to LPTR node
        temp.next = lptr
        lptr, sptr =  sptr, lptr
    
    return res