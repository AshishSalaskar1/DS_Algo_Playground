'''

SOLUTION:
1. Have three ptrs for 0,1,2 (save the heads also if u need, init with Node(-1))
2. Iterate through the LL and add to either of nodes
3. Combining cases
    - If 1 ptr is none: no 1s
        TRUE: zero_ptr.next = one_head
            - check if 2ptrs is none: no 2s
            1. True: optr.next = two_head -> return zero_head.next
            2. False: return zero_head.next
        FALSE:
            1. ones not present but check if twos are present
            -> Twos are there -> optr.next = two_head.next
            -> return zero_head.next

Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printll(root):
    cur = root
    while cur:
        print(cur.data, end="->")
        cur = cur.next
    
    print()

def sortList(head):
    zero_head = Node(-1)
    one_head  = Node(-1)
    two_head = Node(-1)
    
    zptr = zero_head
    optr = one_head
    tptr = two_head

    cur = head
    while cur:
        if cur.data==0:
                zptr.next = cur
                zptr = zptr.next
        elif cur.data==1:
                optr.next = cur
                optr = optr.next
        else:
                tptr.next = cur
                tptr = tptr.next

        cur = cur.next

    zptr.next = None
    optr.next = None
    tptr.next = None
    
    # printll(zero_head)
    # printll(one_head)
    # printll(two_head)

    # there are ones
    if one_head.next is not None:
        zptr.next = one_head.next

        # check if twos are there
        if two_head.next is not None:
            optr.next = two_head.next

        return zero_head.next
    
    else: # no ones but 2s might be present
        if two_head.next is not None:
            optr.next = two_head.next
        return zero_head.next    
    
    

    