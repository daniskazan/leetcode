"""
https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_his_idx_map = {
            num: idx for idx, num in enumerate(nums)
        }
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in nums and num_to_his_idx_map[diff] != idx:
                return [num_to_his_idx_map[diff], idx]
            else:
                continue
