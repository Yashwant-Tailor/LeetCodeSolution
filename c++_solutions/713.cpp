class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int left = 0,right = 0 ;
        int prod = 1 ; 
        int total_cnt = 0 ;
        while (left < nums.size()){
            if (right < left){
                right = left ;
                prod = 1; 
            }
            while (right < nums.size() && nums[right] * prod < k){
                prod *= nums[right] ; 
                right++;
            }
            total_cnt += right - left ;
            prod /= nums[left] ; 
            left++;
        }
        return total_cnt ; 
    }
};
