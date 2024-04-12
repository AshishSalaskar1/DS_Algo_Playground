'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def deleteMiddle(head):
    slow, fast, slow_prev = head, head, None

    # in case LL has only 1 node -> remove that and res=NULL
    if head.next is None:
        return None

    while fast and fast.next:
        slow_prev = slow

        slow = slow.next
        fast = fast.next.next
    
    slow_prev.next = slow_prev.next.next
    return head