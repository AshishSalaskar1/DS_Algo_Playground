"""
ALL PAIR SHORTEST PATH - shortest paths from each node to another
LOGIC: Visit src->dest and check if it can be visited via all nodes as intermediate

For each [src][dest] path, what are the intermediate nodes you can pick (0->V)
- MAT[i][j] = shortest path from i->j
    1. if i==j: mat[i][j] = 0
    2. if edge is present from u->v , mat[u][v] = wt
    3. else float("inf")

- for k in 0->V:
    - for i in 0->V:
        - for j in 0->V: 
            # can you visit i->j via k and its shorter (you can only visit if i->k and k-> are not INF)
            mat[i][j] = min(    
                                    mat[i][j],
                                    mat[i][k] + mat[k][j]
                            )

- DETECT NEGATIVE CYCLES
    1. We assumed that u->u=0 (dist to reach node from itself is 0)
    2. Consider that -ve cycle is present in that case shortes u->u path < 0
        why? u->x-(-3)->y--(1)-->u | u->u = -2
    3. Check in mat if any [i][i] != 0 -> THEN THERE WAS A CYCLE
"""



def floydWarshall(V, m, src, dest, edges):
    # 1 based node indexing
    mat = [[1000000000 for _ in range(V+1)] for _ in range(V+1)]

    for u,v,wt in edges:
        mat[u][v] = wt

    # dist from u->u = 0 
    for node in range(0,V+1):
        mat[node][node] = 0

    for k in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1,V+1):
                if mat[i][k] != 1000000000 and mat[k][j] != 1000000000:
                    mat[i][j] = min(
                        mat[i][j],
                        mat[i][k]+mat[k][j]
                    )
    
    return mat[src][dest]

    
