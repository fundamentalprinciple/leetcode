class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            if (prices[1] - prices[0]) > 0:
                return (prices[1] - prices[0])
            else:
                return 0    

        a,b = 0,1
        flag = True
        profit = 0
        while(flag):
            if (prices[b] - prices[a]) <= 0:
                a,b=b,b+1
            elif (prices[b] - prices[a]) > 0:
                if (prices[b] - prices[a]) > profit:
                    profit = (prices[b] - prices[a])
                    b=b+1
                else:
                    b=b+1
            if b==len(prices):
                flag = False
        return profit
