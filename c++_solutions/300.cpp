/*
This is simple DP solution ( its classic DP problem)
*/
/*
There is nice O(NlogN) solution .
I would reccomend you to check out this solution .
check out this link :
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
*/
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size() ; 
        int ans = 1 ; 
        vector<int>DP(n , 1) ; 
        for(int i = 0 ; i < n ;i++){
            for(int j = i-1 ; j >= 0 ; j--){
                if(nums[i] > nums[j]){
                    DP[i] = max(DP[i] , 1+DP[j]) ; 
                }
            }
            ans = max(ans , DP[i]) ; 
        }
        return ans ; 
    }
};
