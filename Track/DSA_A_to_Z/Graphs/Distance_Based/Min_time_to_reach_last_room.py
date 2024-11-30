"""
Find Minimum Time to Reach Last Room II
Problem: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

SOLUTION:
- DJIKSTRAS 
- (reaching_time, x, y)
- move time varies 1->2->1->2->1

curtime, x, y, move_time = pq.pop()
next_move_time = replace(1->2 and 2->1)

for nbrx,nbry in neighbors:
    # you can reach (vx)(vy) only at time move_times[x][y] or later
    reaching_time = next_move_time +
        max(
            move_times[x][y], # you reached before waittime, so you wait till it happens
            curtime # you have already used more time then waitTime, so directly pick from here (No need to wait)
        )

"""
from queue import PriorityQueue
class Solution:
    def minTimeToReach(self, move_times: List[List[int]]) -> int:
        pq = PriorityQueue()

        n,m = len(move_times), len(move_times[0])

        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        # ( reaching_time, x, y, move_cost)
        pq.put( (0, 0, 0, 2) )

        while pq.qsize() != 0:
            cur_time, x, y, move_cost = pq.get()
            next_move_cost = 1 if move_cost==2 else 2

            if x==n-1 and y==m-1:
                return cur_time
            
            for dx,dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                vx, vy = x+dx, y+dy

                if 0<=vx<n and 0<=vy<m:
                    # you can only move to this node at move_times[i][j]
                    wait_time = move_times[vx][vy]
                    reaching_time = next_move_cost + max(cur_time, wait_time) # you either wait till ur free, or ur reach late (+1 for moving from cur -> this node)

                    if reaching_time < dist[vx][vy]:
                        dist[vx][vy] = reaching_time
                        pq.put( (reaching_time, vx, vy, next_move_cost) )
        
        return dist[n-1][m-1]
