# MULTI SOURCE BFS - LOGICS
- You ideally club a set of nodes into single huge node (practically done by putting all these nodes into the Queue at start)
- Now, you find shortest dist from **ANY OF THESE NODES** to some other node/cell in the matrix
- **You can say that min_dist from this node to ANY_OF_THOSE_NODES is `dist`. BUT: You cant say which nodes was it exactly out of all those nodes**
