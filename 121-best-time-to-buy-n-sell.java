class Solution {
    public int maxProfit(int[] prices) {
        //sliding window with variable size problem.\\

        //int max_profit
        int maxProfit = 0;
        //pointer buy starting at 0
        int buy = 0;
        //pointer sell starting at 1
        int sell = 1;
        //while sell < len(prices)
        while(sell < prices.length){
            //if price at sell < price buy:
            if (prices[sell] < prices[buy]){
                buy = sell;
            } else {
                maxProfit = Math.max(maxProfit, (prices[sell] - prices[buy]));
                sell++;
            }

        }
        return maxProfit;
        //return max_profit
    }
}