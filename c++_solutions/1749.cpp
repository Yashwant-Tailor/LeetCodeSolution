/*
maintain two prefix sum -> min and max 
answer for current prefix sum is -> see the below solution
*/
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size() ; 
        int mi = 0 , ma = 0  ,cur = 0 ; 
        int ans = nums[0] ; 
        for(int i = 0 ; i < n ;i++){
            cur += nums[i] ; 
            ans = max(ans , max(abs(mi - cur) , abs(ma - cur))) ; 
            mi = min(mi , cur) ; 
            ma = max(ma , cur) ;
        }
        return ans ; 
    }
};
