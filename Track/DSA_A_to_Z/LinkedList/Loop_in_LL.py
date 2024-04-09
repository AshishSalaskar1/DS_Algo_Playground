'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # this needs to be after 
        if slow == fast:
            return True

    return False
        