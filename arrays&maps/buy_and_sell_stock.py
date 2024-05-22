class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        min_p = 99999
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            res = max(res, prices[i] - min_p)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
