"""

https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parenth_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for parenth in s:
            if parenth in parenth_map.values():
                stack.append(parenth)
            elif stack and stack[-1] == parenth_map[parenth]:
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("(){}"))