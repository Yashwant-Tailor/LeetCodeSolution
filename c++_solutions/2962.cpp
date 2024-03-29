class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int max_val = *max_element(nums.cbegin(), nums.cend());
        vector<int> max_loc ; 
        max_loc.push_back(-1);
        for (int idx = 0 ; idx < nums.size() ; ++idx){
            if (max_val == nums[idx]){
                max_loc.push_back(idx);
            }
        }
        max_loc.push_back(nums.size());
        long long arr_cnt = 0;
        for (int idx = 1 ; idx <= nums.size() ; ++idx){
            if (idx+k-1 < max_loc.size()){
                arr_cnt += ((long long)max_loc[idx]-max_loc[idx-1]) * ((long long)nums.size() - max_loc[idx+k-1]);
            }
        }
        return arr_cnt ;
    }
};
