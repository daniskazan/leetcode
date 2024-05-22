from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        class X:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)

            def __hash__(self):
                # Create a hash based on the sorted items of the dictionary
                return hash(tuple(sorted(self.__dict__.items())))

            def __eq__(self, other):
                # Check equality based on the dictionary items
                return self.__dict__ == other.__dict__

        res = defaultdict(list)
        for s in strs:
            ma = Counter(s)
            x = X(**ma)
            res[x].append(s)
        return list(res.values())
