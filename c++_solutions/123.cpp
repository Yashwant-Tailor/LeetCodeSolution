/*
same as solution in which we allowed to do one transaction 
but here we will add make the second transaction cost minimum add the difference of two (local minima to local maxima)
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size() ; 
        int profit2 = 0 , profit1 = 0 , buy1  = INT_MAX  , buy2 = INT_MAX ; 
        for(int i = 0 ; i < n  ; i++){
            profit1 = max(profit1 , prices[i] - buy1) ; 
            buy1 = min(buy1 , prices[i]) ; 
            
            buy2  = min(buy2 , prices[i] - profit1) ; 
            profit2 = max(profit2 , prices[i] - buy2) ; 
        }
        return profit2 ; 
    }
};
