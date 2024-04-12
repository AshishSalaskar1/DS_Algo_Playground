'''
SOLUTION 1: BRUTE
- Find length of LL
- Then iterate once again and remove N-K+1 th node

SOLUTION 2: O(N)
- slow=head, fast=head+k
- move slow, head by 1, when fast reaches NULL, slow will be the node to be removed
- You will have to have to maintain prev for SLOW (or use fast.next -> dont let it go to null)
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    slow, fast, slow_prev = head, head, None

    for _ in range(k):
        fast = fast.next

    if fast is None: # in case you need to remove head itself (fast will race past LL n become null)
        head = head.next
        return head

    while fast and slow:
        slow_prev = slow
        fast = fast.next
        slow = slow.next

    
    slow_prev.next = slow_prev.next.next
    return head

def removeKthNodeSlower(head, k):
    nll = 0

    # FIND LENGTH
    cur = head
    while cur:
        cur = cur.next
        nll += 1
    
    # FIND WHICH NODE TO REMOVE
    target_idx = nll-k
    # print(nll, target_idx)

    # REMOVE THE NODE
    cur, prev = head, None
    cur_count = 0
    while cur:
        if cur_count == target_idx: # remove this node
            if cur == head: # in case you need to remove the ROOT node
                return cur.next

            prev.next = cur.next
            return head
        prev = cur
        cur = cur.next
        cur_count += 1
    
    return head
    
        