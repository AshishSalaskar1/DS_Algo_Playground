class Node:
    def __init__(self, key=0, val=0, freq=1, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_from_dll(self, node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def insert_into_dll(self, node: Node) -> Node:
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        return node

    def remove_head(self) -> Node:
        if self.size == 0:
            return None
        return self.remove_from_dll(self.head.next)


class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.freq = {}  # {freq: DLL}
        self.min_freq = 0
        self.hmap = {}  # {key: Node}

    def update_node_freq(self, node: Node) -> None:
        freq_of_node = node.freq

        # remove from current freq DLL
        self.freq[freq_of_node].remove_from_dll(node)
        if self.freq[freq_of_node].size == 0:
            if self.min_freq == freq_of_node:
                self.min_freq += 1

        # update node's frequency
        node.freq += 1

        # add it to the new freq DLL
        if node.freq not in self.freq:
            self.freq[node.freq] = DLL()
        self.freq[node.freq].insert_into_dll(node)

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.update_node_freq(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.c == 0:
            return

        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.update_node_freq(node)
        else:
            if len(self.hmap) >= self.c:
                min_freq_dll = self.freq[self.min_freq]
                node_to_remove = min_freq_dll.remove_head()
                del self.hmap[node_to_remove.key]

            new_node = Node(key, value)
            self.hmap[key] = new_node
            if 1 not in self.freq:
                self.freq[1] = DLL()
            self.freq[1].insert_into_dll(new_node)
            self.min_freq = 1
