/*
start from index i = 0 
step 1: from current index find a local minimum in array buy stock on that day
step 2: from this find the next local maximum which is adjacent to current local minimum and sell the stock on that day
step 3: repat this process from step 1 unitll you reach the end of the array
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0 , buy_stock_price = INT_MAX  , sell_stock_price = INT_MIN, n = prices.size(); 
        for(int i = 0 ; i < n-1 ; i++){
            if(buy_stock_price < prices[i] && prices[i] > prices[i+1]){
                profit += prices[i] - buy_stock_price ; 
                buy_stock_price = INT_MAX ; 
                continue ;
            }
            if(buy_stock_price > prices[i]){
                buy_stock_price = prices[i] ;
            }
        }
        if(buy_stock_price < prices[n-1]){
            profit += prices[n-1] - buy_stock_price ;
        }
        return profit ; 
    }
};
