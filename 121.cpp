class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_stock_price = prices[0] , n = prices.size() ; 
        int ans = -1 ; 
        for(int i =1 ; i < n ; i++){
            // we have two possible choice on a particular day
            // cell the stock on given day using the minimum price we got in previous days
            ans = max(ans , prices[i] - min_stock_price) ; 
            // buy the stock if the previous minimum stock price is greater than 
            // the stock price on current day 
            // so that we can earn more profit by selling this stock in some future day
            min_stock_price = min(min_stock_price , prices[i] ) ; 
        }
        // if we have loss i.e. ans < 0 then return zero
        if(ans < 0){
            return 0 ;
        }
        return ans ; 
    }
};
