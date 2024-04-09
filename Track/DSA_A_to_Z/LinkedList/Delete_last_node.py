"""
Solution 1: Find len of linked list and then iterate till n-1

Solution 2: While iterating mantain both prev2, prev and cur pointers

"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(node: Node) -> Node:
    cur = node
    prev = None
    prev_2 = None

    while cur.next.next is None:
        prev_2 = prev
        prev = cur
        cur = cur.next

    prev_2.next = None
    return node

# without prev, prev2
def deleteLast(node: Node) -> Node:
    cur = node
    prev = None

    while cur.next.next:

        prev = cur
        cur = cur.next

    cur.next = None
    return node