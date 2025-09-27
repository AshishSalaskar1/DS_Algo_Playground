"""
https://leetcode.com/contest/biweekly-contest-166/problems/maximize-alternating-sum-using-swaps/description/
"""
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)

        # Build adjacency list
        for u, v in swaps:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        total_sum = 0

        def dfs(start):
            stack = [start]
            indices = []
            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                indices.append(node)
                for nei in graph[node]:
                    if not visited[nei]:
                        stack.append(nei)
            return indices

        # Process each connected component
        for i in range(n):
            if not visited[i]:
                indices = dfs(i)

                # Numbers in this component
                values = [nums[j] for j in indices]

                # Count even/odd slots
                even_slots = sum(1 for j in indices if j % 2 == 0)
                odd_slots = len(indices) - even_slots

                # Sort values descending
                values.sort(reverse=True)

                # Largest go to evens, smallest to odds
                values_for_even = values[:even_slots]
                values_for_odd = values[even_slots:]

                total_sum += sum(values_for_even) - sum(values_for_odd)

        return total_sum