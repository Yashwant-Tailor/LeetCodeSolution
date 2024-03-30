class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        unordered_map<int,int> freq ;
        int l = 0, r1 =0 ,r2 = 0 ;
        int arr_cnt = 0;
        while (l < nums.size()){
            while (r1 < nums.size() && freq.size() < k){
                if (freq.find(nums[r1]) != freq.end()){
                    freq[nums[r1]] += 1 ; 
                }
                else{
                    freq[nums[r1]] = 1;
                }
                if (r2 == r1){
                    r2++ ;
                }
                r1++ ;
            }
            while (r2 < nums.size() && freq.find(nums[r2])!=freq.end()){
                r2++;
            }
            if (freq.size() == k){
                arr_cnt += r2-r1+1 ;
            }
            freq[nums[l]] -= 1 ;
            if (freq[nums[l]] == 0){
                freq.erase(nums[l]);
            }
            l++;
        }
        return arr_cnt; 
    }
};
