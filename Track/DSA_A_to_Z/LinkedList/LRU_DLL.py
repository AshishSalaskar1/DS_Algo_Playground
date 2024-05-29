"""
Problem:  Implment get, put methods in Least Recently Used Cache - LRU
- Both get() and put() MUST BE O(1)

Soln Video: https://www.youtube.com/watch?v=Xc4sICC8m4M&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=78
- Here [most_recent ..... least_recent] is used, but we are using reverse notation here

INTUITION:
=> Why list cant be used to store lru and DLL is needed?
- You dont only keep on inserting but need to delete also (in case of get() on already seen)
Example: [least_recent, .... , most_recent]
1. put(1) -> [1] # consider adding also as a hit/access
2. put(2) -> [1,2]
3. put(3) -> [1,2,3]
4. get(2) -> [1,3,2] # You remove 2 and put it at last (There is delete+update always)

-> If you remove from list (it will take O(n) time, search + delete)
- But we need both get() and put() in O(1)

SOLUTION
- HMAP stores {key:Node}, DLL has tail and head (tail: used to add most recent, head: used to pop LRU)
- DLL represents: [least_recent, .... , most_recent]
- HEAD and TAIL are dummy nodes such that head.next=LRU and tail.prev = MRU (most recently used)

- delete_from_cache(self, key)
    - get actual node = hmap[key] (pop it from hmap)
    - You directly have the node now -> use prev,next ptrs to remove this node from DLL
    - return node.val

- insert_into_cache(self, key, val)
    - You want to insert this node in hmap + update this as most recent used
    - Push it to LAST index (just before tail)
        - Update next of tail.prev
        - Update prev of tail
        - Udate prev and next of new Node
    - Add the new Node to hmap

=> GET(key)
- if key is prsent in hmap:
    - surely you need to delete from DLL and put it at last + udpate new Node in hmap
    - val = delete_from_cache(key)
    - insert_into_cache(key,val)
    return val
- else:
    return -1 (NOT FOUND)

=> PUT (key,va)
- If its present -> update the caches + hmap (Same key but diff value can be set, each set is also recent use)
- IF PRESENT in HMAP -> delete_from_cache(key) 
- insert_into_cache(key,val) [You insert both present(it was popped in last step) or not(newly added)]
- After inserting if len(hmap) > capacity:
    # LRU node is right next to HEAD
    delete_from_cache(head.next.key)
"""

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


                        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)