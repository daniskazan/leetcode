
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1
        res_lst = [1] * len(nums)

        for i in range(len(nums)):
            res_lst[i] *= left_product
            left_product *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            res_lst[i] *= right_product
            right_product *= curr
        return res_lst


if __name__ == '__main__':
    s = Solution()

    print(s.productExceptSelf(nums=[1,2,3,4]))
