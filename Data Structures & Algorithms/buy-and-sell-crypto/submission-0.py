class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                diff=prices[j]-prices[i]
                if diff>0 and diff>maxPrice:
                    maxPrice=diff
        return maxPrice