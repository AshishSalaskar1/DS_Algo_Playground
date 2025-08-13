# Linked List Cheatsheet (verbatim)

Reverse Nodes in k-Group (from LinkedList/Reverse_LL_in_K_groups.py)
```python
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
```

LRU Cache with DLL + HashMap (from LinkedList/LRU_DLL.py)
```python
class Node:
    def __init__(self,key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.hmap = {}

        # Q [least_recent ...... most_recent]
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def delete_from_cache(self, key: int) -> int:
        """
        Remove NODE from CACHE + MAP and send back the val (SINCE YOU REMOVE IT FROM BOTH)
        """
        node = self.hmap.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.val
    
    def insert_into_cache(self, key: int, val: int) -> None:
        """
        Insert node in hmap, push it into Q from back
        """
        # H <-> 1 <-> 2 <-> T
        node = Node(key,val) #  2 <- Node -> T
        node.prev = self.tail.prev
        node.next = self.tail

        # set one node before Tail
        self.tail.prev.next = node # H <-> 1 <-> 2 -> Node | 2<-T->null

        # set prev of Tail
        self.tail.prev = node # H <-> 1 <-> 2 <-> Node <-? tail | 2<-T->null  

        self.hmap[key] = node

    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.delete_from_cache(key)
            self.insert_into_cache(key, val)
            return val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.hmap:
            self.delete_from_cache(key)
        
        self.insert_into_cache(key, val)

        if len(self.hmap) > self.c: # evict LRU -> first
            self.delete_from_cache(self.head.next.key) # insert after head
```

Check Palindrome Linked List (from LinkedList/Is_Palindrome_LL.py)
```python
def reverse_ll(head):
    cur = head
    prev = None

    while cur is not None:
        temp_next = cur.next
        cur.next = prev

        prev = cur
        cur = temp_next
        
    
    return prev


def isPalindrome(head):

    slow_prev = None
    slow, fast = head, head

    while fast and fast.next:
        slow_prev = slow 
        slow = slow.next
        fast = fast.next.next

    mid = slow
    slow_prev.next = None
    mid_head = reverse_ll(mid)

    p1, p2 = head, mid_head
    # why only p1? In case odd LL-> you reverse from MID and MID need not be considered
    # 1->2->3->4->5 = [1->2->null] [5->4->3->NULL]
    while p1 is not None:
        if p1.data != p2.data:
            return False
        
        p1 = p1.next
        p2 = p2.next
    
    return True
```

Merge two sorted linked lists (two approaches) (from LinkedList/Merged_2_sorted_LL.py)
```python
def sortTwoLists(first, second):
    new_head = None
    cur_ptr = new_head

    # set head to smallest head
    if first.data <= second.data:
        new_head = first
        first = first.next
    else:
        new_head = second
        second = second.next
    
    cur_ptr = new_head

    while first and second:
        if first.data <= second.data:
            cur_ptr.next = first
            cur_ptr = cur_ptr.next
            first = first.next
        else:
            cur_ptr.next = second
            cur_ptr = cur_ptr.next
            second = second.next
        
    # one of this might be left
    if first is None or first.next is None:
        while second:
            cur_ptr.next = second
            cur_ptr = cur_ptr.next
            second = second.next
    
    if second is None or second.next is None:
        while first:
            cur_ptr.next = first
            cur_ptr = cur_ptr.next
            first = first.next
        
    return new_head

# IN-PLACE and faster

def sortTwoLists(first, second):
    if first is None:
        return second

    if second is None:
        return first
    
    if first.data <= second.data:
        sptr,lptr = first, second
    else:
        sptr, lptr = second, first

    # this is needed to return
    res = sptr

    while sptr is not None and lptr is not None:
        # point one point behind sptr
        temp = None

        # increment sptr untill its greater than lptr (STABLE)
        while sptr and sptr.data <= lptr.data:
            temp = sptr
            sptr = sptr.next
        
        # point last node in smaller LL to LPTR node
        temp.next = lptr
        lptr, sptr =  sptr, lptr
    
    return res
```

---

## 🗺️ Quick map
- 🐢🐇 Fast/slow patterns
- 🔁 Reversal building blocks
- 🧩 Merge/split/use sentinels

## ✅ Study checklist
- [ ] Handle len<k in k-group reverse?
- [ ] Restore structure when required (palindrome)?
- [ ] O(1) LRU ops via DLL+map invariant maintained?
