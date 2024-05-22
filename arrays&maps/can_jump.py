class Solution:
    def canJump(self, nums: list[int]) -> bool:
        final_pos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= final_pos:
                final_pos = i
        return final_pos == 0


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
