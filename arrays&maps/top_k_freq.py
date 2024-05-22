class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter

        c = Counter(nums)

        res = []
        l = sorted(c.items(), key=lambda x: x[1], reverse=True)
        for num, freq in l[:k]:
            res.append(num)
        return res





if __name__ == '__main__':
    s = Solution()

    print(s.topKFrequent([1,2,2,3,3,3, 4], 2))