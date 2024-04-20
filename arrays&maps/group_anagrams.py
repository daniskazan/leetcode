from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                count[idx] += 1
            res[tuple(count)].append(s)
        return res.values()



if __name__ == '__main__':
    s = Solution()

    print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
