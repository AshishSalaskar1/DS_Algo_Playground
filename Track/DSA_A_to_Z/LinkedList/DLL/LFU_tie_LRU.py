"""
PROBLEM: https://leetcode.com/problems/lfu-cache/
- GET(key), PUT(key,val)


ASK
- Both get() and put() consider as one hit ( for least recent calculation )
- When your Cache capacity is full, you need to evict the LEAST FREQUENTLY HIT/USED <k,v> pair
    1) If there is only 1 LRU pair -> evict that
    2) If there are multiple LRU pais -> Use LRU to decide what to evict between them


INTUITION ( mostly from LRU problem)
- You have GET -> so surely you need a hashamp for mapping <key: Node(key,val,freq)>
- You need LRU so surely some kind of DLL is needed

IDEA 1: Use a freqMap -> <freq: DLL> | Here DLL is all nodes that currently has frequency = freq
IDEA 2: minFreq can be easily tracked ( no sorting is needed)
    - When a new element gets added -> that becomes minFreq=1
    - When a element gets hit -> then the minFreq can change (+1) only if that was the minFreq

UPDATE_FREQ
- Whenever you hit a already present node (get/put) you need to do 2 things
    1) Update its freq - remove it from the freqMap[curFreq] and put it into freqMap[curFreq+1]
    2) Update the minFreq if it changes. Check if freqMap[curFreq]==0 and this was your minFreq -> only then change it 
    

=> GET
1. Check if the node is present using hmap else -1
2. Update the hit freq using UPDATE_FREQ

=> PUT
1. If the key is already present
    1. Fetch the node using hmap[key]
    2. Replace the node.key ( because same key but value might be same or can change also)
    3. UPDATE_FREQ(node)
2. If its a new node and EVICTION is need
    1. freqmap[minFreq].pop_lru_node() -> this handles both cases (if only 1 returns, if not returns HEAD node i.e LRU node)
    2. remove the popped node from hmap
3. Create a new node -> add it in the hashmap -> set minFreq=1 as every new node gets added to freq=1




"""
class Node:
    def __init__(self, key=None, val=None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 1

class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_into_dll(self, node: Node):
        # INSERT AT END -> MOST RECENTLY USED
        node.prev = self.tail.prev
        self.tail.prev.next = node

        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def delete_from_dll(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
    
    def pop_lru_node(self):
        # return 1st node from LEFT/head
        lru_node = self.head.next
        self.delete_from_dll(lru_node)

        return lru_node

    
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freqmap = {} # freq: DLL
        self.hmap = {} # key: Node
        self.minFreq = 0

    def update_freq(self, node):
        curfreq = node.freq
        self.freqmap[curfreq].delete_from_dll(node)

        newfreq = node.freq + 1
        node.freq += 1

        # put it in on freq above)
        if newfreq not in self.freqmap:
            self.freqmap[newfreq] = DLL()
        
        self.freqmap[newfreq].insert_into_dll(node)

        # CHECK IF PREVFREQ is now empty ( because if >0 other pairs may have same freq so it still remains the minFreq)
        if self.freqmap[curfreq].size == 0 and self.minFreq == curfreq:
            self.minFreq += 1


    def get(self, key):
        result = -1
        if key in self.hmap:
            result = self.hmap[key].val
            self.update_freq(self.hmap[key])
        
        return result
    
    def put(self, key, val):
        if self.capacity == 0:
            return

        # check if its there -> Update val and then update_frequency
        if key in self.hmap:
            node = self.hmap[key]
            node.val = val # same key but VALUE might change
            self.update_freq(node)
            return
        
        # YOU NEED TO INSERT A NEW NODE
        newnode = Node(key, val)

        # CHECK IF EVICT
        if len(self.hmap) >= self.capacity:
            popped_node = self.freqmap[self.minFreq].pop_lru_node()
            self.hmap.pop(popped_node.key)


        # NEW NODE -> freq = 1
        if 1 not in self.freqmap:
            self.freqmap[1] = DLL()

        self.hmap[key] = newnode
        self.freqmap[1].insert_into_dll(newnode)
        self.minFreq = 1
