"""
PROBLEM: Maximum Twin Sum of a Linked List
- https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

EXAMPLES:
1. 5->4->2->1
- twins = (5+1), (4,2) [Basically, first and last pairs]

SOLUTION
5->4->2->1
1. Find mid and mid_prev
    - mid_prev = 4 (used to attach second half after reversing second half)
    - mid = 2
2. Reverse second half | reverse starting from mid
    - 5->4 | null<-2<-1
    - mid_prev.next = prev => 5->4->1->2->null

3. fptr=head, sptr=mid
5->4->1->2->null [5,1]
^     ^
f     s

5->4->1->2->null [4,2]
   ^     ^
   f     s  
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast, mid_prev = head, head, None
        res = 0

        # find MID and MID_PREV node 
        while fast and fast.next:
            mid_prev = slow
            slow = slow.next
            fast = fast.next.next
        mid = slow # slow points to mid (we also need node before this for attaching reversed node)

        # REVERSE SECOND HALF
        cur, prev = mid, None
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        mid_prev.next = prev
        
        # iterate both half together
        first_half_ptr = head
        second_half_ptr = mid_prev.next

        while second_half_ptr is not None:
            res = max(res, first_half_ptr.val+second_half_ptr.val)
            first_half_ptr = first_half_ptr.next
            second_half_ptr = second_half_ptr.next
        
        return res