class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        array of prices
        find greatest difference between buy and sell
        
        var to store max profit 

        create two pointers buy and sell

        iterate through prices while sell not grater than len of prices
        check if buy >= sell: #know it's not a good day to buy
            buy = sell
        if sell - price is greater than max_profit, update max profit
            sell += 1
        
        return max profit


        """

        buy = 0
        sell = 1
        max_profit = 0


        while sell <= len(prices) - 1:
            if prices[buy] >= prices[sell]:
                buy = sell
            
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, (prices[sell] - prices[buy]))

            sell += 1

        return max_profit
















