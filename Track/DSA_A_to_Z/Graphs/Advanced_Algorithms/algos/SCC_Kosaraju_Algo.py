"""
https://www.youtube.com/watch?v=R6uoSjZ2imo


SCC - Strongly Connected components
- Set/Island of nodes, where for any pair (u,v) -> there is path from u->v and v->u

KOSARAJU IDEA
- You can think of graph as a set of islands (SCCs) connected via bridges (edges between SCCs)
    - | SCC 1 | ----bridge---> | SCC 2 | ----bridge---> | SCC 3 |
    - If start DFS() from any node in SCC 1, you can reach all nodes in SCC 1, and also reach SCC 2 and SCC 3 via the bridges.
    - However, if you start DFS() from SCC 3, you cannot reach SCC
    - MAIN PART: You need to figure out which node/SCC to start DFS from, so that you can cover all other SCCs/nodes.
- Now, within each SCC, all nodes are mutually reachable. 

- If we reverse the direction of all edges in the graph, the SCCs remain unchanged, but the direction of the bridges between them is reversed.
    - | SCC 1 | <----bridge---- | SCC 2 | <----bridge---- | SCC 3 |
    - Now if run dfs(any node in SCC 1), you can only reach nodes in SCC 1 but not SCC 2 or SCC 3.

    MAIN IDEA: 
        - Order matters: You need to dfs(SCC1) -> dfs(SCC2) --> dfs(SCC3) in the original graph to cover all nodes.
        - How to find which bridge edges to reverse? Dont worry -> reverse all edges. ( because within SCC all nodes are mutually reachable even if u reverse)


💡 STEPS:
1. GET ORDER: Perform a DFS on the original graph, keeping track of the order in which nodes finish (i.e., when all their neighbors have been visited). This can be done using a stack.
2. REVERSE GRAPH: Reverse the direction of all edges in the graph.
3. DFS ON REVERSED GRAPH: Pop nodes from the stack one by one and perform DFS on the reversed graph. Each time you start a new DFS from a popped node, you discover

💡 SCC on Disconnected Graphs:
- Just apply dfs for each unvisited node in the original graph while getting order (step 1)


"""


from collections import defaultdict

class Kosaraju:
    def get_scc(self, edges: list[list], V: int) -> int:
        adj = defaultdict(list)
        revadj = defaultdict(list)
        for u,v in edges: 
            adj[u].append(v)
            revadj[v].append(u)


        def dfs(node: int, adj_list: dict, store_order: bool = False):
            seen.add(node)
            for nbr in adj_list[node]:
                if nbr not in seen: dfs(nbr, adj_list, store_order)
                    
            if store_order:
                order_stack.append(node) # DFS ENDS FOR THIS NODE HERE
            else:
                cur_taken.append(node)

        

        # STEP 1: Order based on time when DFS ends for each nodes -> gives which node to visit first
        seen = set()
        order_stack = []
        # this is to account disconnect graphs
        for node in range(V):
            if node not in seen: dfs(node, adj, True)


        # STEP 2: reverse edges
        # Already stored in `revadj``

        # STEP 3: Run dfs on each node -> each SCC will be an island 
        # scc_count = 0
        scc = []
        seen = set()
        cur_taken = list()
        while order_stack:
            node = order_stack.pop()
            if node not in seen:
                dfs(node, revadj, False)
                scc.append(cur_taken.copy());cur_taken = list()

        return len(scc),scc


v=5
edges = [[0,2],[0,3],[1,0],[2,1],[3,4]] #3
print(Kosaraju().get_scc(edges=edges, V=v)) # (3, [[2, 1, 0], [3], [4]])


v=8
edges = [[0,1],[1,2],[2,0],[2,3],[3,4],[4,5],[4,7],[5,6],[6,7],[6,4]] #4
print(Kosaraju().get_scc(edges=edges, V=v)) # (4, [[1, 2, 0], [3], [5, 6, 4], [7]])

