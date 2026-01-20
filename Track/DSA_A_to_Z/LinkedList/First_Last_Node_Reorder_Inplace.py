# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
PROBLEM: https://leetcode.com/problems/reorder-list/

STEP 1: Find mid ( in case of even second mid)
STEP 2: BREAK INTO TWO
STEP 3: Reverse Second half
STEP 4: Merge like 2 sorted linked lists


EXAMPLE 1: 1->2->3->4->5
MID: |3|
BREAK:   1->2->3 | 4->5
REVERSE: 1->2->3 | 5->4
COMBINE:
    - LEFT: 1->2->3
    - RIGHT: 5->4
RES = 1->5->2->4->3 ( Pick one from each )

EXAMPLE 2: 1->2->3->4
MID: |3|
BREAK:   1->2->3 | 4
REVERSE: 1->2->3 | 4
COMBINE:
    - LEFT: 1->2->3
    - RIGHT: 4
RES = 1->4->2->3 ( Pick one from each )
"""
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev, next = None, None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        head = head
        
        # STEP 1: Find mid of linked list ( Second mid in case its even length)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2: Break in 2 halves -> Reverse second half
        second_half_head = self.reverse(slow.next)
        slow.next = None #  Break both the sections


        # STEP 3: Merge both halves ( Just like Merge two sorted linked lists)
        lhead, rhead = head, second_half_head

        while rhead:
            lnext, rnext = lhead.next, rhead.next
            lhead.next = rhead
            lhead.next.next = lnext
            
            lhead = lnext
            rhead = rnext
        
        




          

        
         
        