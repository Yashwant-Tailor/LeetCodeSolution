/*
DP[i][j] = will true if we can obtain totalsum = i , till index (1 to j)
*/
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = 0 ; 
        for(int i = 0 ; i < nums.size() ; i++){
            totalSum += nums[i] ; 
        }
        if(totalSum%2){
            return false ;
        }
        totalSum /= 2 ; 
        vector<vector<bool>>DP(totalSum +1 , vector<bool>((int)nums.size() , false)) ; 
        for(int i = 0 ; i < nums.size() ; i++){
            DP[0][i] = true ;
        }
        for(int i = 1 ; i <= totalSum  ; i++){
            for(int j = 0 ; j < nums.size() ; j++){
                if(j-1>=0 && DP[i][j-1]){
                    DP[i][j] = true ;
                }
                if(i - nums[j] >= 0 && j-1>=0 &&  DP[i-nums[j]][j-1]){
                   DP[i][j] = true ; 
                }
            }
        }
        int n = nums.size() ; 
        return DP[totalSum][n-1] ; 
    }
};
