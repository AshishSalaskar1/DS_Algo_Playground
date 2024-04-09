class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# 4<->2<->5<->1

def constructDLL(arr: [int]) -> Node:
    root = Node(arr[0])

    cur = root

    for x in arr[1:]:
        new_node = Node(x)
        new_node.prev = cur
        cur.next = new_node

        cur = new_node

    return root


def deleteLastNode(head: Node) -> Node:
    cur = head

    # only single node
    if cur.next is None:
        return None

    while cur.next.next:
        cur = cur.next

    cur.next = None
    return head