"""
https://www.codingninjas.com/studio/problems/course-schedule-ii_1069243
Two questions are being asked
1. Can you schedule | Is this a DAG (because only a DAG can have Topological order)
2. Return Order if possible

SOLUTION 1:
- Step 1: Check if cycle present in cycle -> if yes -> its not DAG -> no Topo order
- Step 2: Do Topo sort using BFS+Kahns or DFS+Stack

SOLUTION 2:
- Directly do Kahns algo (In degree approach), in case cycle is present ur topo_sort answer wont contain all the nodes
- In this case if len(topo_sort) != V => NO TOPO SORT

"""

def topologicalSort(adj, v):
    vis = set()
    topo_sort = []
    indegs = [0 for _ in range(v)]

    q = []
    for node in range(v):
        for nbr in adj[node]:
                indegs[nbr] += 1

    for i in range(v):
        if indegs[i] == 0:
            q.append(i)
            vis.add(i)

    # BFS
    while len(q) != 0:
        curr = q.pop(0)
        # added cur node with nothing incoming to topological sorted order
        topo_sort.append(curr)

        for nbr in adj[curr]:
            if nbr not in vis:
                indegs[nbr] -= 1

                # in case this node doesnt have any incoming edges add to Q
                # since all nodes leading to this have been added in topo
                if indegs[nbr] == 0:
                    q.append(nbr)
                    vis.add(nbr) # here vis means -> this nodes parents were all added n this also got added in topo sort


    topo_sort = [x+1 for x in topo_sort]
    
    if len(topo_sort) == v:
        return topo_sort
    else: # cycle present
        return []

def findSchedule(numCourses, prerequisites):    
    # 1 to 0 indexing
    adj = [[] for _ in range(numCourses)]
    for course, pre_req in prerequisites:
        adj[pre_req-1].append(course-1)
        
    return topologicalSort(adj=adj, v=numCourses)