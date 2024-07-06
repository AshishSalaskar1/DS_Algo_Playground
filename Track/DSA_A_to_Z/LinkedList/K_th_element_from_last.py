class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
N = 10, k = 2
1. Make slow point to 2nd node
2. Then take another ptr at 1, and increment both
3. Slow would reach "k" nodes faster than "base", that means base points to the (n-k)th node
"""

def get_last_kth_node(self, head: ListNode, k) -> ListNode:
    print(k)
    slow, base = head, head
    k_prev = None
    for _ in range(k):
        if slow.next:
            slow = slow.next
    
    while slow:
        k_prev = base
        slow = slow.next
        base = base.next
    

    return k_prev, base