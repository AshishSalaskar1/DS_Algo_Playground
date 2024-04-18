# Input: N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output: b d a c

# Input: N = 3, K = 3
# dict = {"caa","aaa","aab"}

"""
Intuition behind getting order:
    - Compare between two subsequent strings, first char mismatch means bcoz of this char s1 came earlier than s2
    - So char1 -> char2 (char2 comes after char1)
    
Toposort:
    - Run simple topo sort on these adjacency list

When you cant create dict
1. s2 comes after s1, but len(s2)>len(s1) - this doesnt make any sense 
2. Edge case -> in case some char does have any dependency (it becomes single island in the graph) -> just add it before topo sort order
"""


def topo_sort(arr, k , adj):
    n = len(adj)
    q = []
    vis = set()
    indegs = {}
    res = []

    for u,vs in adj.items():
        if u not in indegs:
            indegs[u] = 0
        for v in vs:
            indegs[v] = indegs.get(v,0) + 1

    for node, indegree in indegs.items():
        if indegree == 0:
            q.append(node)
            vis.add(node)


    while len(q) != 0:
        node = q.pop(0)
        res.append(node)
        for nbr in adj.get(node,[]):
            indegs[nbr] -= 1

            if indegs[nbr] == 0:
                q.append(nbr)
                vis.add(nbr)
    return res


def get_adj(arr, k):
    adj = {}
    for i in range(len(arr)-1):
        s1, s2 = arr[i], arr[i+1]
        # iterate smaller string
        for i in range(min(len(s1),len(s2))):
            if s1[i] != s2[i]: #s1[i] > s2[i] in dictionary
                adj[s1[i]] = [*adj.get(s1[i],[]), s2[i]]
                break

    return adj

def alien_dict(arr, k):
    adj = get_adj(arr, k)
    return topo_sort(arr, k , adj)


arr = ["baa","abcd","abca","cab","cad"]
N = len(arr)
k = 4 # no of alphabets in the dictionary
print(alien_dict(arr, k))

arr = ["caa","aaa","aab"]
N = 3
K = 3 # no of alphabets in the dictionary
print(alien_dict(arr, k))
