
class Node:
    def __init__(self, key, val, prev, next) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 0

class DLL:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_from_cache(self, node: int) -> None:
        """
        Remove current node from DLL 
        """
        # PREV <-> NODE <-> NEXT
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_into_cache(self, key: int, val: int) -> Node:
        """
        Create new node and insert at last - most recent
        """
        node = Node(key, val)

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

        return node

    def remove_lru_node(self) -> Node:
        lru_node = self.head.next
        self.remove_from_cache(lru_node)
        return lru_node



class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.hmap = {} # {key:Node}
        self.freq = {} # {freq: DDL(dll, head, tail )}
        self.min_freq = 0
    
    def updateNode(self, node: Node) -> None:
        """
        get() or put() called on Node, update frequency of node and move it to relevant DLL
        """
        # get the frequency of this node (from node.freq) -> find the DLL with that frequency -> You get the DLL
        # from that DLL remove node

        # increment min_freq (if the current freq list is empty)  -> min_freq+=1 (also update freq of current node)
        # add this node to freq+1's DLL (append OR new DLL with only this node)
        # udpate the hmap

    def get(self, key: int) -> int:
        if key in self.hmap:
            # updateNode()
    
            pass
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key already present -> update_node(hmap[key] -> replace key -> then send to update)
        
        # KEY NOT PRESENT
        # create new Node() -> freq=0, put it in freq[0]'s DLL (maybe be empty or already some elements)
        # hmap[key] = newNode
        # update minFreq = min(minFreq, 0)
        

        pass


"""
Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

LFUCache(2)
put(1,1)
put(2,2)
get(1) => 1
put(3,3)
get(2) => -1
get(3) => 3
put(4,4)
get(1) => -1
get(3) => 3
get(4) => 4
"""
