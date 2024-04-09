'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

# 1 -> 2 -> 3 -> 4
#  None <- 1  2 -> 3 -> 4

def reverseLinkedList(head):
    prev, cur = None, head

    while cur is not None:
        # save your next node
        next_node = cur.next

        
        cur.next = prev #cur.next = prev 
        prev = cur 
        cur = next_node
        
    return prev # cur will be None after exiting while loop

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''
# 4 <-> 3 <-> 2 <-> 1.

def reverseDLL(head):
    prev, cur = None, head

    while cur:
        next_node = cur.next

        cur.next = prev
        cur.prev = next_node

        prev = cur
        cur = next_node

    
    return prev

