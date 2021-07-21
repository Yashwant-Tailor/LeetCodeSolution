/*
simple DP problem 
*/
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<long long int>DP(n , INT_MAX) ; 
        DP[0]  = 1 ;
        for(int i = 1 ; i < n ; i++){
            int thresold = DP[i-1] ; 
            for(int j = 0 ; j < i ; j++){
                if(DP[j]*2 > thresold){
                    DP[i] = min(DP[i] , DP[j]*2) ; 
                }
                if(DP[j]*3 > thresold){
                    DP[i] = min(DP[i] , DP[j]*3) ; 
                }
                if(DP[j] * 5 > thresold){
                    DP[i] = min(DP[i] , DP[j]*5) ; 
                }
            }
        }
        return (int)DP[n-1] ; 
    }
};
