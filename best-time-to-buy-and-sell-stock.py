# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    #left = buy, right = sell        
    l, r = 0 #setting 2 variables to represent left and right. initialized at 0
    maxP = 0 #setting the max profit to 0

    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            


maxProfit([7,1,5,3,6,4])
