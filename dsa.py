def find_max_pairs(nums):
    nums.sort()
    left = 0
    right = len(nums) - 1
    max_pairs = 0

    while left < right:
        s = nums[left] + nums[right]
        pairs = 0

        while left < right and nums[left] + nums[right] == s:
            pairs += 1
            left += 1
            right -= 1

        max_pairs = max(max_pairs, pairs)

    return max_pairs

nums = [1, 1, 3, 4, 2, 2]
max_pairs = find_max_pairs(nums)
print("Maximum number of pairs:", max_pairs)
