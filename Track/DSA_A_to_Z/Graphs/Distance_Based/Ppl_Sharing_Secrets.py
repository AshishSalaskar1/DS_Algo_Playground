"""
https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2025-12-19


SOLUTIONS:
1. BFS | DFS - TLE
2. UF -> WORKS
"""
from heapq import heapify, heappush, heappop
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Queue for BFS. It will store (person, time of knowing the secret)
        q = []
        heapify(q)

        heappush(q, (0,0)) # (user, when_did_he_learn_secret)
        heappush(q, (firstPerson, 0))

        # Do BFS
        while q:
            person, time = heappop(q)
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    heappush(q, (next_person, t))

        # Since we visited only those people who know the secret,
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]