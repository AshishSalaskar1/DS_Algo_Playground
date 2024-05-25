"""
GREAT DOC: https://bradfieldcs.com/algos/trees/priority-queues-with-binary-heaps/

====== MIN HEAP ======
INTUTION:
=> Complete Binary Tree
- Represent the heap as a Complete Binary Tree using a LIST (Nodes in all levels except last)
- In such cases you insert value sequentially
- In CBT, (i) has 2 children (2*i -> left child) and (2*i+1 -> right child)
- Initially, items = [0], size = 0 (to make it simpler, else children would be 2i+1, 2i+2)

=> MIN HEAP PROPERTY
- Parent(items[i]) must be smaller then left_child(items[2i]) and right_child(items[2i+1])

=> INSERT (val)
- You first insert it at last -> last value in tree | size += 1
- From inserted_node to root, check if you violate min_heap property and resolve
- PROPAGATE DOWN -> UP (since last node doesnt follow minheap property)
    1. cur = self.size
    2. check all child,parent relationships and swap wherever the Min Heap property gets voilated

=> PEEK
- Return items[1] -> first element will be min, since we follow min_heap_property for each operation

=> POP
- popped_val = items[1]
- Swap last node to first: items[1] = items[self.size] and items.pop() 
    - You are removing last element since its already placed at items[1]
- PROPOGATE Root -> leaf (since fist_node[newly swapped with last node] doesnt follow minheap property)
    cur = 1
    1. For each parent (i) 
        - minchild_i = minimum of left and right node (in some case right node may not exist, since last levels may not be filled in CBT)
        - If items[i] > items[minchild_i]: Violates min_heap_property
            swap(parent, minchild_i)
        cur = minchild_i
            
==> TIME COMPLEXITIES
- PEEK -> O(N) # you directly return items[1]
- INSERT -> O(logn) = O(nlogn)
    1. You first insert at last - O(1)
    2. You then balance from ROOT <- LEAF - O(logn)
- POP -> O(logn) = O(nlogn)
    1. You first swap(first,last) and pop last one - O(1)
    2. You then balance from ROOT -> LEAF - O(logn)
- Build Heap from list having `n` nodes:
    1. Simple doing insert for each - O(nlogn)
    2. Optimized way given the list at once - O(n)

"""

class MaxHeap:
    def __init__(self) -> None:
        self.items = [0] # 0 is considered to be dummy/len=0
        self.size = 0

    def _propagate_up(self):
        i = self.size
        while i//2 > 0: # you have parents of nodes
            # child > parent | Violates the maxHeap Property
            if self.items[i] > self.items[i//2]:
                self.items[i], self.items[i//2] = self.items[i//2], self.items[i]
            i = i//2

    def _propagate_down_from_root(self):
        i = 1
        while i*2 < self.size: # atleast one child exists -> left child will be there (complete binary Tree)
            mchild = self._get_max_child(i) # return min_index of smallest child (i*2 ir i*2+1)
            if self.items[i] < self.items[mchild]: # parent > min_child => HEAP VIOLATED
                self.items[i], self.items[mchild] = self.items[mchild], self.items[i]
            i = mchild

    def _get_max_child(self, i):
        # right child doesnt exist (since it complete Binary Tree)
        if i*2 + 1 > self.size: # left child exists n hence its min
            return i*2

        # now both Left and Right childrens exist
        if self.items[i*2] < self.items[i*2+1]: #left is smaller
            return i*2+1
        else: # right will be smaller
            return i*2


    def insert(self, val: int) -> None:
        """
            Adds an item with val into the MinHeap
        """
        print(f"Inserted {val}....")
        self.items.append(val) # just insert at last
        self.size += 1

        # Rebalance/Remaintain heap property bottom up
        self._propagate_up()

    def peek(self) -> int:
        return self.items[1]

    def pop(self) -> int:
        """
         Pops the minimum most element and then rebalances the heap
        """
        print(f"Popping {self.items[1]}")
        i = 0
        # replace first/min element with last element -> delete last node ->Rebalance
        min_popped_item = self.items[1]
        self.items[1] = self.items[self.size]
        self.items.pop()

        self.size -= 1
        self._propagate_down_from_root()
        return min_popped_item

heap = MaxHeap()
for x in [10,20,15,5,8,1]:
    heap.insert(x)
    print(heap.items)

while heap.size != 0:
    heap.pop()
    print(heap.items)



