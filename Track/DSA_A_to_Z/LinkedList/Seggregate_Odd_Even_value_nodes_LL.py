==> ODD EVEN BASED ON INDEXES (Leetcode)


==> ODD EVEN BASED ON VALUES
'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def segregateEvenOdd(head):
    even_ptr = None
    even_ptr_head = None
    odd_ptr = None
    odd_ptr_head = None

    cur = head
    while cur  is not None:
        if cur.data%2 == 0:
            if even_ptr is None: # first even node found
                even_ptr = cur
                even_ptr_head = even_ptr
            else:
                even_ptr.next = cur
                even_ptr = even_ptr.next
        else:
            if odd_ptr is None: # first odd node found
                odd_ptr = cur
                odd_ptr_head = odd_ptr
            else:
                odd_ptr.next = cur
                odd_ptr = odd_ptr.next
        
        cur = cur.next
    
    # IMP: Since you keep on adding cur, cur may still have right links
    even_ptr.next = None
    odd_ptr.next = None
    even_ptr.next = odd_ptr_head

    return even_ptr_head


