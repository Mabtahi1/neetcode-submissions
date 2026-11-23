class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                CurrProf = prices[r] - prices[l]
                maxProf = max(maxProf, CurrProf)

            else:
                l = r

            r += 1
            
        return maxProf            