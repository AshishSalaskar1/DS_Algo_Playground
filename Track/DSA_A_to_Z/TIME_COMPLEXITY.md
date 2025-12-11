# Time Complexity Reference Guide

A comprehensive reference for time and space complexities of common data structures and algorithms.

## 📊 Data Structures

### Arrays
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Access | O(1) | - | Direct index access via memory address |
| Search (Unsorted) | O(n) | - | Must check each element |
| Search (Sorted) | O(log n) | - | Use binary search |
| Insert at End | O(1) | - | Amortized O(1) for dynamic arrays |
| Insert at Beginning | O(n) | - | Requires shifting all elements |
| Delete at End | O(1) | - | No shifting required |
| Delete at Beginning | O(n) | - | Requires shifting all elements |
| Delete at Index | O(n) | - | Worst case when deleting at start |

### Linked List
| Operation | Singly Linked | Doubly Linked | Notes |
|-----------|---------------|---------------|-------|
| Access | O(n) | O(n) | Must traverse from head |
| Search | O(n) | O(n) | No random access like arrays |
| Insert at Head | O(1) | O(1) | Only pointer updates needed |
| Insert at Tail | O(1)* | O(1) | *Singly: needs tail pointer |
| Insert at Index | O(n) | O(n) | O(n) to reach position + O(1) insert |
| Delete at Head | O(1) | O(1) | Simple pointer update |
| Delete at Tail | O(n) | O(1) | Singly: need previous node |
| Delete at Index | O(n) | O(n) | Doubly: can traverse backwards |

### Stack
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Push | O(1) | Add to top only |
| Pop | O(1) | Remove from top only |
| Peek/Top | O(1) | View top without removal |
| Search | O(n) | Not efficient, use HashMap instead |
| IsEmpty | O(1) | Check size or top pointer |

### Queue
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Enqueue | O(1) | Add to rear |
| Dequeue | O(1) | Remove from front |
| Front/Peek | O(1) | View front element |
| Rear | O(1) | View rear element |
| IsEmpty | O(1) | FIFO: First In First Out |

### Hash Table / Hash Map
| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Search | O(1) | O(n) | Worst case: all keys hash to same bucket |
| Insert | O(1) | O(n) | Requires rehashing when load factor exceeded |
| Delete | O(1) | O(n) | Same as search complexity |
| Space | O(n) | O(n) | Extra space for handling collisions |

### Binary Search Tree (BST)
| Operation | Average | Worst Case | Balanced (AVL/Red-Black) | Notes |
|-----------|---------|------------|--------------------------|-------|
| Search | O(log n) | O(n) | O(log n) | Worst case: skewed tree (linked list) |
| Insert | O(log n) | O(n) | O(log n) | Self-balancing trees prevent skewing |
| Delete | O(log n) | O(n) | O(log n) | Complex with 2 children (find successor) |
| Inorder Traversal | O(n) | O(n) | O(n) | Gives sorted order |
| Space | O(n) | O(n) | O(n) | Recursion stack: O(h) where h = height |

### Binary Tree
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Level Order Traversal (BFS) | O(n) | Uses queue, processes level by level |
| Preorder/Inorder/Postorder (DFS) | O(n) | Visits each node once |
| Height | O(n) | Must visit all nodes in worst case |
| Search (Unbalanced) | O(n) | No ordering property unlike BST |
| Space (Recursion) | O(h) where h = height | Best: O(log n), Worst: O(n) for skewed |

### Heap (Min/Max Heap)
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Find Min/Max | O(1) | Root element is always min/max |
| Insert | O(log n) | Insert at end, bubble up |
| Delete Min/Max | O(log n) | Replace root with last, bubble down |
| Heapify | O(n) | Build heap from array (bottom-up) |
| Decrease/Increase Key | O(log n) | Update and restore heap property |
| Space | O(n) | Usually implemented as array |

### Trie (Prefix Tree)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Insert | O(m) | O(m × n) | m = word length, create nodes for each char |
| Search | O(m) | - | Traverse m nodes |
| Prefix Search | O(m) | - | Excellent for autocomplete features |
| Delete | O(m) | - | Check if node can be safely deleted |

*m = length of word, n = number of words

### Segment Tree
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Build | O(n) | O(4n) ≈ O(n) | Build from bottom-up |
| Query (Range) | O(log n) | - | Efficient range queries (sum, min, max) |
| Update (Point) | O(log n) | - | Update single element |
| Update (Range) | O(log n) | - | With lazy propagation |

### Fenwick Tree (Binary Indexed Tree)
| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| Build | O(n log n) | O(n) | Can be optimized to O(n) |
| Query (Prefix Sum) | O(log n) | - | Sum from index 0 to i |
| Update (Point) | O(log n) | - | Update single element |
| Range Query | O(log n) | - | query(r) - query(l-1) |

### Disjoint Set Union (Union-Find)
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Find | O(α(n))* | With path compression |
| Union | O(α(n))* | With union by rank/size |
| Connected | O(α(n))* | Check if same parent |

*α(n) is the inverse Ackermann function, practically O(1)

## 🔍 Searching Algorithms

| Algorithm | Best | Average | Worst | Space | Notes |
|-----------|------|---------|-------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | Works on unsorted arrays |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Requires sorted array |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Jump by √n blocks, then linear |
| Interpolation Search | O(1) | O(log log n) | O(n) | O(1) | Best for uniformly distributed data |

## 🔄 Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Best when nearly sorted |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always O(n²), minimal swaps |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Efficient for small/nearly sorted |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Consistent performance, external sorting |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Worst case with bad pivot, cache-friendly |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place, not stable |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Only for integers in small range |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes | Process digit by digit |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes | Good for uniformly distributed data |

*k = range of input, d = number of digits

## 📈 Graph Algorithms

### Graph Representations
| Representation | Space | Add Edge | Check Edge | Get All Edges | Notes |
|----------------|-------|----------|------------|---------------|-------|
| Adjacency Matrix | O(V²) | O(1) | O(1) | O(V²) | Better for dense graphs, wastes space |
| Adjacency List | O(V+E) | O(1) | O(V) | O(V+E) | Better for sparse graphs, space efficient |

*V = vertices, E = edges

### Graph Traversal
| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| BFS (Breadth First Search) | O(V + E) | O(V) | Uses queue, finds shortest path (unweighted) |
| DFS (Depth First Search) | O(V + E) | O(V) | Uses stack/recursion, good for connectivity |

### Shortest Path Algorithms
| Algorithm | Time Complexity | Space | Use Case | Notes |
|-----------|----------------|-------|----------|-------|
| Dijkstra's (Min Heap) | O((V+E) log V) | O(V) | Non-negative weights | Fails with negative weights |
| Bellman-Ford | O(V × E) | O(V) | Negative weights, detects cycles | Slower but handles negative edges |
| Floyd-Warshall | O(V³) | O(V²) | All pairs shortest path | DP approach, works with negative edges |
| 0-1 BFS | O(V + E) | O(V) | Only 0 and 1 weights | Uses deque, faster than Dijkstra |

### Minimum Spanning Tree
| Algorithm | Time Complexity | Space | Notes |
|-----------|----------------|-------|-------|
| Kruskal's (Union-Find) | O(E log E) | O(V) | Sort edges, add if doesn't form cycle |
| Prim's (Min Heap) | O((V+E) log V) | O(V) | Grow tree from starting vertex |

### Other Graph Algorithms
| Algorithm | Time Complexity | Space | Notes |
|-----------|----------------|-------|-------|
| Topological Sort (DFS) | O(V + E) | O(V) | Only for DAG, uses DFS + stack |
| Topological Sort (Kahn's) | O(V + E) | O(V) | BFS-based, uses in-degree |
| Cycle Detection (Undirected) | O(V + E) | O(V) | Using DFS/BFS/Union-Find |
| Cycle Detection (Directed) | O(V + E) | O(V) | Use DFS with recursion stack |
| Strongly Connected Components (Kosaraju's) | O(V + E) | O(V) | Two DFS passes, transpose graph |
| Articulation Points | O(V + E) | O(V) | Vertex whose removal disconnects graph |
| Bridges | O(V + E) | O(V) | Edge whose removal disconnects graph |

## 🎯 Dynamic Programming Patterns

| Pattern | Typical Complexity | Space Optimization | Notes |
|---------|-------------------|-------------------|-------|
| 1D DP | O(n) | O(n) → O(1) | Use variables for previous states |
| 2D DP | O(n × m) | O(n × m) → O(m) | Keep only current and previous row |
| 3D DP | O(n × m × k) | O(n × m × k) → O(m × k) | Keep only current 2D slice |
| LIS (Binary Search) | O(n log n) | O(n) | Patience sorting approach |
| LCS | O(n × m) | O(min(n, m)) | Classic 2D DP problem |
| Matrix Chain Multiplication | O(n³) | O(n²) | Try all possible splits |
| Knapsack (0/1) | O(n × W) | O(W) | Each item used once |
| Knapsack (Unbounded) | O(n × W) | O(W) | Items can be reused |
| Edit Distance | O(n × m) | O(min(n, m)) | Insert/Delete/Replace operations |
| DP on Trees | O(n) | O(n) | DFS + memoization |

## 🔢 String Algorithms

| Algorithm | Time Complexity | Space | Use Case | Notes |
|-----------|----------------|-------|----------|-------|
| KMP (Pattern Matching) | O(n + m) | O(m) | Pattern search | Build LPS array, no backtracking |
| Rabin-Karp (Rolling Hash) | O(n + m) avg, O(nm) worst | O(1) | Multiple pattern search | Hash collisions cause worst case |
| Z-Algorithm | O(n + m) | O(n + m) | Pattern matching | Z-array stores longest match from i |
| Manacher's Algorithm | O(n) | O(n) | Longest palindrome | Expand around center with optimization |
| Longest Palindromic Substring (DP) | O(n²) | O(n²) | Find longest palindrome | Check all substrings |

## 🎲 Mathematical Algorithms

| Algorithm | Time Complexity | Notes |
|-----------|----------------|-------|
| GCD (Euclidean) | O(log(min(a,b))) | Recursive: gcd(a,b) = gcd(b, a%b) |
| Prime Check (Trial Division) | O(√n) | Check divisibility up to √n |
| Sieve of Eratosthenes | O(n log log n) | Find all primes up to n |
| Modular Exponentiation | O(log n) | Compute (a^b) % m efficiently |
| Matrix Multiplication | O(n³) | Strassen's: O(n^2.807) |
| Fast Fourier Transform (FFT) | O(n log n) | Polynomial multiplication |

## 🎨 Advanced Techniques

### Two Pointers
| Pattern | Time Complexity | Notes |
|---------|----------------|-------|
| Two Sum (Sorted) | O(n) | Start from both ends, move based on sum |
| Three Sum | O(n²) | Fix one, use two pointers for rest |
| Container With Most Water | O(n) | Move pointer with smaller height |

### Sliding Window
| Pattern | Time Complexity | Notes |
|---------|----------------|-------|
| Fixed Size Window | O(n) | Window size k, slide by 1 |
| Variable Size Window | O(n) | Expand/shrink based on condition |

### Prefix Sum
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Build Prefix Array | O(n) | prefix[i] = prefix[i-1] + arr[i] |
| Range Sum Query | O(1) | sum(l,r) = prefix[r] - prefix[l-1] |

### Binary Search on Answer
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Search Space [L, R] | O(log(R-L) × f(x)) | Binary search on monotonic function |

*f(x) = time to check if answer is valid

### Monotonic Stack/Queue
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Next Greater Element | O(n) | Each element pushed/popped once |
| Largest Rectangle in Histogram | O(n) | Use monotonic increasing stack |
| Sliding Window Maximum | O(n) | Use deque, maintain decreasing order |

## 🎯 Bit Manipulation

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Check if Bit Set | O(1) | n & (1 << i) |
| Set Bit | O(1) | n \| (1 << i) |
| Clear Bit | O(1) | n & ~(1 << i) |
| Toggle Bit | O(1) | n ^ (1 << i) |
| Count Set Bits | O(log n) | Brian Kernighan's algorithm |
| Power of 2 Check | O(1) | n & (n-1) == 0 |

## 📝 Notes

- **Best Case**: Minimum time required (often when input is already in desired state)
- **Average Case**: Expected time for random input
- **Worst Case**: Maximum time required (often used for analysis)
- **Space Complexity**: Extra space required (excluding input)
- **Amortized**: Average time per operation over sequence of operations

### Common Time Complexity Order (Fastest to Slowest)
```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### When to Use What?

| Complexity | Approx Max n | Typical Use | Notes |
|------------|-------------|-------------|-------|
| O(1) | Any | Direct access, math formulas | Constant time regardless of input |
| O(log n) | 10¹⁸ | Binary search, divide & conquer | Halving search space each step |
| O(√n) | 10¹⁴ | Prime check, factorization | Check up to square root |
| O(n) | 10⁸ | Single pass, linear scan | Process each element once |
| O(n log n) | 10⁶ | Sorting, divide & conquer | Most efficient comparison sorts |
| O(n²) | 10⁴ | Nested loops, simple DP | Check all pairs |
| O(n³) | 500 | Triple nested loops, Floyd-Warshall | Check all triplets |
| O(2ⁿ) | 20-25 | Backtracking, subset generation | Exponential growth, all subsets |
| O(n!) | 10-12 | Permutations, brute force | Factorial growth, try all orders |
