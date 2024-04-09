

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    slow, fast = head, head

   # IMP: CHECK ONLY FAST
   # WHY F at (3)->4 : F=f.next,next=null, 
   # Next iter: slow is not None but fast.next (Next of None)    
    while fast and fast.next:
        print(slow.data, fast.data)
        slow = slow.next
        fast = fast.next.next

    return slow