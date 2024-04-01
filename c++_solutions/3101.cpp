class Solution {
public:
    long long countAlternatingSubarrays(vector<int>& nums) {
        long long arr_cnt = 0 ;
        int idx = 0 ;
        int prev_num = nums[0] ;
        int l = 0 , r = 0;
        while (idx < nums.size()){
            long long arr_len = 1;
            int curr_num = nums[idx] ; 
            idx++;
            while (idx < nums.size() && curr_num != nums[idx]){
                arr_len++;
                curr_num = nums[idx] ; 
                idx++;
            }
            arr_cnt += (arr_len * (arr_len+1))/2 ; 
        }
        return arr_cnt ; 
    }
};
