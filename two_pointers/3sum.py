

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        hmap = {num: idx for idx, num in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                desired = -nums[i] - nums[j]
                if desired in hmap.keys() and hmap[desired] != i and hmap[desired] != j:
                    res.add(tuple(sorted([nums[i], nums[j], desired])))
        return [list(x) for x in res]


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))