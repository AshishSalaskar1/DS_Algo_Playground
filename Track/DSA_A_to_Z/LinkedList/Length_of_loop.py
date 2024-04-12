class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


"""
- Loop using slow, fast appraoch
- Increment fast.next and see when you reach the same point again
"""


def lengthOfLoop(head: Node) -> int:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cur_fast = fast
            fast = fast.next
            loop_len = 1

            while fast != cur_fast:
                fast = fast.next
                loop_len += 1
            return loop_len
    
    return 0
            

