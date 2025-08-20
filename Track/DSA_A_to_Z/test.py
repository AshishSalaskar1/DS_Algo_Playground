"""
Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4



"""
class Node:
    def __init__(self, key=None, val=None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, size: int):
        self.capacity = size
        self.hmap = {} # KEY -> NODE(key,val,prev,next)

         # HEAD<->OLDEST<->x<->--------<->NEWEST<->TAIL
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def insert_into_cache(self, key: int, val: int):
        node = Node(key, val)
        
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node


    def delete_from_cache(self, key: int):
        node = self.hmap[key]

        next_node = node.next
        prev_node = node.prev

        prev_node.next = prev_node
        next_node.prev = prev_node

    def get(self, key: int):
        result = -1
        if key in self.hmap:
            result = self.hmap[key].val
            self.delete_from_cache(key)
            self.insert_into_cache(key, result)

        return result

    def insert(self, key: int, val: int):
        # You treat INSERT as "DELETE" -> "INSERT" at back
        # Else you would have pick it out -> and then insert it at the end ( this is the same delete and insert again in the end)
        if key in self.hmap:
            self.delete_from_cache(key)

        self.insert_into_cache(key, val)

        # delete the oldest: HEAD<->OLDEST<->x<->--------<->NEWEST<->TAIL
        if len(self.hmap)>self.capacity:
            self.delete_from_cache(self.head.next.key)



lRUCache = LRUCache(2);
lRUCache.insert(1, 1); # cache is {1=1}
lRUCache.insert(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.insert(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.insert(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4
