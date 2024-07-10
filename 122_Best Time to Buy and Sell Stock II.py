class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)

        for i in range(1,n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    
obj = Solution()
result = obj.maxProfit([1,2,3,4,5])
print(result)
