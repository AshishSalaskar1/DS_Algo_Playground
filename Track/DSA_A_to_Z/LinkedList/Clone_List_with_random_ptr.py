"""
Problem: https://leetcode.com/problems/copy-list-with-random-pointer/

Solution Explaination: https://leetcode.com/problems/copy-list-with-random-pointer/solutions/4003262/9792-hash-table-linked-list-by-vanamsen-boof


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hmap = {}

        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            hmap[cur].next = hmap.get(cur.next) # can be NONE also
            hmap[cur].random = hmap.get(cur.random)
            cur = cur.next

        return hmap[head]
        