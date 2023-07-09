/*
Simple DP problem 
try to think in terms of recursion and then use DP to avoid same calculation again and again
*/
class Solution {
public:
    int climbStairs(int n) {
        vector<int>DP(n+1 , 0) ; 
        DP[0]  = 1 ; 
        for(int i = 1 ; i <= n ; i++){
            if(i == 1){
                DP[i] = DP[i-1] ; 
            }
            else{
                DP[i] = DP[i-1] + DP[i-2] ; 
            }
        }
        return DP[n] ; 
    }
};
