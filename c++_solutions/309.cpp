/*
DP problem 
max_profit[i] = maximum profit we can get till i'th day
transition :
let say we will sell a stock on day i , then we will find the most optimal day for buying one stock from (1 to i-1) and then we make the transition
assume we sell one stock on day i and buy one stock on day j (its clear that i > j i.e. we have buy a stock before selling it)
if we do this transaction then max_profit[i] = max(max_profit[i] , price[i] - price[j] + max_profit[j-2]) , here for cooldown day we can't use max_profit[j-1] so we will use max_profit[j-2] ; 
if we don't do this transaction then max_profit[i] = max(max_profit[i] , max_profit[j]) ; 
*/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size() ; 
        vector<int>max_profit(n+2 , 0) ; 
        for(int i = 2 ; i < n +2; i++){
            for(int j = i-1 ; j >= 2 ; j--){
                max_profit[i] = max(max_profit[j] , max(max_profit[i] , prices[i-2] - prices[j-2] + max_profit[j-2]) ); 
            }
        }
        return max_profit[n+1] ; 
    }
};
