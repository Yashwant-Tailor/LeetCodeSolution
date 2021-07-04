/*
there are three state required for the complete solution
at iteration i do the following
state 1 : minimum product if we multiply this number in a contigous non-empty array till i-1 iteration
state 2: maximum ......
state 3: if we don't multiply this number than the product is equal to this number 
look at the solution for transition of this states
*/
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size()  , ans = nums[0] ; 
        vector<vector<int>>DP(n , vector<int>(3 , 1)) ; 
        DP[0][0] = DP[0][1] = DP[0][2] = nums[0] ; 
        for(int i = 1 ; i < n ;i++){
            DP[i][0] = min(DP[i-1][0] , min(DP[i-1][1] , DP[i-1][2])) * nums[i];
            DP[i][1] = max(DP[i-1][0] , max(DP[i-1][1] , DP[i-1][2])) * nums[i] ; 
            DP[i][2] = nums[i] ; 
            ans = max(ans , max(DP[i][0] , max(DP[i][1] , DP[i][2]))) ; 
        }
        return ans ; 
    }
};
