

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter

        freq = [[] for _ in range(len(nums)+1)]
        c = Counter(nums)

        for num, occurancy in c.items():
            freq[occurancy].append(num)

        res = []
        for i in range(len(freq), 0, -1):
            for elem in freq[i]:
                res.append(elem)
                if len(res) == k:
                    return res


        return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1], 1))