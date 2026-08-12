class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        maxx = 0 
        sumh=0
        for i in range(len(prices)):
            if i+1<len(prices) and prices[i]<prices[i+1]:
                c =prices[i+1]-prices[i]   
                sumh+=c
        return sumh        