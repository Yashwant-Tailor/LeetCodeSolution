/*
solution complexity O(N*sqrt(N))
*/
class Solution {
public:
    int numSquares(int n) {
        vector<int>DP(n + 1 , INT_MAX) ; 
        DP[0] = 0 ,DP[1] = 1 ; 
        for(int i =  1 ; i <= n ; i++){
            for(int j = 1 ;  j*j <= i ; j++){
                DP[i] = min(DP[i]  , DP[i - j*j] + 1) ; 
            }
        }
        return DP[n] ; 
    }
};
