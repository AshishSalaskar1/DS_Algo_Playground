# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
https://leetcode.com/problems/sort-list/

OPTIMAL SOLUTION: MERGE SORTS

STEP 1: Keep on splitting in half till only 1 element in left
STEP 2: When returning back start merging slowly


(4 -> 2 -> 1 -> 3) -> SPLIT
(4 -> 2) (1 -> 3) -> SPLIT
(4) (2) (1) (3) -> SPLIT
== CANT SPLIT ANYMORE == START MERGING
(4) MERGE (2) | (1) MERGE (3)
(2 -> 4) MERGE (1 -> 3)
(1 -> 2 -> 3 -> 4)

"""
class Solution:
    def findmid(self, head: ListNode) -> ListNode:
        """
            return one node before mid -> so that you can split
        """
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        return prev

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        newhead = ListNode(0)  # dummy node
        cur = newhead

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        cur.next = left if left else right
        
        return newhead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        midnode = self.findmid(head)
        secondhead = midnode.next
        
        midnode.next = None # split from center
        left = self.sortList(head)
        right = self.sortList(secondhead)
    
        # START MERGING
        return self.merge(left, right)
        