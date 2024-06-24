# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        if head is None or head.next is None:
            return None

        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        
        prev.next = prev.next.next
        return head
        