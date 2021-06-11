// simple DP problem
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size() ; 
        vector<int>DP(n , INT_MAX) ; 
        DP[0] = 0 ; 
        for(int i = 0 ; i < n ; i++){
            for(int j = i+1 ; j <= min(n-1 , i+nums[i]) ; j++){
                DP[j] = min(DP[j] , DP[i] +1) ; 
            }
        }
        return DP[n-1] ; 
    }
};
