/*
simple DP bottom up  approach .
*/
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size() ; 
        vector<int>DP(n , 0) ; 
        DP[0]  = triangle[0][0]  ; 
        for(int i = 1  ; i < n ; i++){
            for(int j = i ; j >= 0  ; j--){
                if(j == 0){
                    DP[j] = DP[j] + triangle[i][0] ; 
                }
                else if(j == i){
                    DP[j] =  DP[j-1] + triangle[i][j];
                }
                else{
                    DP[j]  = min(DP[j] , DP[j-1]) + triangle[i][j]  ;
                }
            }
        }
        int mi = INT_MAX ; 
        for(int i = 0 ; i < n ;i++){
            mi = min(mi , DP[i]) ; 
        }
        return mi ; 
    }
};
