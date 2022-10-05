# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    #left = buy, right = sell        
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else: buy = sell
            sell +=1
        return max_profit

maxProfit([7,1,5,3,6,4])
