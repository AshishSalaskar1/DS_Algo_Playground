"""
Problem: https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/

Solution: https://leetcode.com/problems/find-k-th-smallest-pair-distance/solutions/5632765/o-n-log-n-n-log-w-binary-search-sliding-window-java-c-python-go-rust-javascript/

"""
class Solution:
    def countPairsWithinDistance(self, arr: List[int], target: int) -> int:
        count = left = 0
        for right in range(1, len(arr)):
            while arr[right] - arr[left] > target:
                left += 1
            count += right - left
        return count

    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        # k smallest => there are k-1 elements lesser than the answer
        # 1 smalelst => there are 0 elements lesser than the answer
        # 4 smallest => there are 3 elements lesser than the answer
        numbers.sort()
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        while minDistance < maxDistance:
            mid = (minDistance + maxDistance) // 2
            if self.countPairsWithinDistance(numbers, mid) < k:
                minDistance = mid + 1
            else:
                maxDistance = mid
        
        return minDistance

    