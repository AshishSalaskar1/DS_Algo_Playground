"""
Solution:
1. Slow, fast approach to find cycle
2. In case you find cycle, take another pointer ENTRY=head
3. Move both SLOW and ENTRY one-by-one untill they meet (GAURANTEED)
"""

'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    if head == None or head.next == None:
        return None

    fast, slow, entry = head, head, head
    while fast  and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next

            return slow

    return None