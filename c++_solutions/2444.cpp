class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long arr_cnt = 0 ; 
        int ls_min = 0 ,ls_max = 0 ,ls_out = 0;
        for (int i = 1 ; i <= nums.size() ; ++i){
            if (nums[i-1] == minK){
                ls_min = i ;
            }
            if (nums[i-1] == maxK){
                ls_max = i ;
            }
            if (nums[i-1] < minK || nums[i-1] > maxK){
                ls_out = i ;
            }
            arr_cnt += max(0 , min(ls_min , ls_max) - ls_out) ;
        }
        return arr_cnt ; 
    }
};
