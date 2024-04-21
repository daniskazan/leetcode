from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, n in enumerate(numbers, start=1):
            hashmap[n] = idx

        for idx, num in enumerate(numbers, start=1):
            diff = target - num
            if diff in hashmap.keys() and hashmap[diff] != idx:
                return [idx, hashmap[diff]]


if __name__ == '__main__':
    print(Solution().twoSum([0,0,3,4], 0))