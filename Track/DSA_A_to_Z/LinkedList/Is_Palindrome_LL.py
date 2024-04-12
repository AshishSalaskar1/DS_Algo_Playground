'''
SOLUTION:
1. Find mid of linkedlist, reverse second half 
2. Keep one pointer at start and one at new mid (after reversing second half)
3. Check if all ele in FIRST HALF are EQUAL to second half

Example 1: 1->2-> |3| ->2->1
- mid: 3, prev_mid=2 => new_rev_head=1
- 1->2->null | 1->2->3->null
- p1=head, p2 = new_rev_head


Example 2: 1->2->2->1
- mid: 2, prev_mid=2 (second 2) => new_rev_head=1
- 1->2->null | 1->2->null
- p1=head, p2 = new_rev_head
- p1=head, p2 = new_rev_head


Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverse_ll(head):
    cur = head
    prev = None

    while cur is not None:
        temp_next = cur.next
        cur.next = prev

        prev = cur
        cur = temp_next
        
    
    return prev

def isPalindrome(head):

    slow_prev = None
    slow, fast = head, head

    while fast and fast.next:
        slow_prev = slow 
        slow = slow.next
        fast = fast.next.next

    mid = slow
    slow_prev.next = None
    mid_head = reverse_ll(mid)

    p1, p2 = head, mid_head
    # why only p1? In case odd LL-> you reverse from MID and MID need not be considered
    # 1->2->3->4->5 = [1->2->null] [5->4->3->NULL]
    while p1 is not None:
        if p1.data != p2.data:
            return False
        
        p1 = p1.next
        p2 = p2.next
    
    return True
