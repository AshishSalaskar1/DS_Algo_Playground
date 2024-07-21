"""
ROTATE LINKED LIST
https://leetcode.com/problems/rotate-list/

Example:
1->2->3->4->5 
k=2
1. 5->1->2->3->4
2. 4->5->1->2->3

SOLUTION
-> Rotate Array by k places: 1 2 3 4 5 
1. Reverse [0,n-k][n-k+1] => [1 2 3] [4 5] => [3 2 1] [5 4]
2. Reverse [0,n] => [3 2 1 5 4] => [4 5 1 2 3]

LL LOGIC
1->2->3->4->5
1. Break into 2 LL (for reversing)
    1->2->3 => 3->2->1 
    4->5 => 5->4
2. Join back
    3 -> 2 -> 1 -> 5 -> 4
3. Reverse
    4 -> 5 -> 1 -> 2 -> 3

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse_ll(self, head: ListNode) -> None:
        """
        Reverse LL from head -> end (head might be in middle also)
        """
        tail = head
        cur, prev = head, None

        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur

            cur = temp_next
        
        return prev, head
    

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, cur = 0, head

        # find n and update k if k>n
        while cur:
            cur = cur.next
            n += 1

        if n==0 or k==0 or k%n==0:
            return head
        k = k%n
        
        
        # get (n-k+1)th node
        cur, prev = head, None
        for _ in range(n-k): # (n-k) because it will be one point ahead 
            prev = cur
            cur = cur.next
        
        r1, r1_end, r2 = head, prev, cur

        # detach both parts
        r1_end.next = None # will cause infinite loop

        # reverse [0,n-k] and [n-k+1, n]
        r1_head, r1_tail = self.reverse_ll(r1)
        r2_head, r2_tail = self.reverse_ll(r2)

        # attach both parts back
        r1_tail.next = r2_head

        # reverse whole LL again
        result_head, result_tail = self.reverse_ll(r1_head)
        return result_head


        
        