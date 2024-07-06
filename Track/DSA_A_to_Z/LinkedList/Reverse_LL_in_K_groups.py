"""
Problem: Reverse Nodes in k-Group

SOLUTION

1->2->3->4->5 (k=3)
SOLVE(1)
- Move head by 3 elements
1) REVERSE K groups 
    [1->2->3] -LINK BROKEN-> 4->5
    [3->2->1] -LINK BROKEN-> 4->5
2) [3->2->1] -> SOLVE(4) ===> [3->2->1->4->%]

SOLVE(4)
1) Move head by 3 elements => it becomes None since len(4->5)=2 < 3
return 4->5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head: ListNode) -> None:
        tail = head
        cur, prev = head, None

        while cur:
            temp_next = cur.next
            cur.next = prev
            prev = cur
            cur = temp_next
        
        return prev, tail
    
    def solve(self, head: ListNode, k: int) -> ListNode:
        cur = head
        for _ in range(k-1): # you want to point to the kth node, not k+1 the
            if cur:
                cur = cur.next
        # in case cur=None, means the LL is of size < k
        
        if cur: # remaining LL >= k size
            temp_next = cur.next
            cur.next = None # break link for reversing
            cur_head, cur_tail = self.reverse_ll(head)
            cur_tail.next = self.solve(temp_next, k) # next reversing
            return cur_head

        else: # remaining LL is < k size -> dont touch anything
            return head


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head is None or head.next is None:
            return head

        return self.solve(head, k)
        