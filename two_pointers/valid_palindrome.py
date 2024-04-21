class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        s = "".join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))