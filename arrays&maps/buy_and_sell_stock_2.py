"""
122. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

if __name__ == '__main__':
    s = Solution()
    print()