"""
PQ SOLUTION:
- Store all heads in a PQ
- Pop the min_node and add it to res -> now add min_node.next to PQ
- Keep on continuing

PYTHONIC CHALLENGE
- PQ needs items that needs to be comparable and here we need node.val and node itself
- Since ListNode itself is class which cant be compared (otherwise it would be <node.val, ListNode>)
- Build a wrapper class `ItemListNode` and implement `__lt__(self, other)` function for comparison
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue
class ItemListNode:
    def __init__(self, ll_node: ListNode):
        self.node = ll_node
    
    def __lt__(self, other: ListNode):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lls: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = PriorityQueue()
        for ll in lls:
            if ll:
                print(ll, ll.val, ll.next)
                pq.put(ItemListNode(ll))
        
        if pq.qsize() == 0:
            return None
        
        res = ListNode()
        res_head = res

        while pq.qsize() > 0:
            min_node = pq.get().node # returns node with smallest value
            print(min_node.val)
            
            if min_node and min_node.next: # if node exists -> add it to PQ
                pq.put(ItemListNode(min_node.next))
            
            # point res -> min_node (min_node -> NULL)
            min_node.next = None
            res.next = min_node
            res = res.next
            
        
        return res_head.next
            
            
        