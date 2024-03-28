class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        map<int,int> freq ;
        int max_len =  0;
        int left = 0 ,right = 0;
        while (right < nums.size()){
            if (freq[nums[right]] < k){
                freq[nums[right]]++;
                max_len = max(max_len , right-left+1);
                right++;
            }
            else{
                freq[nums[left]]--;
                left++;
            }
        }
        return max_len ; 
    }
};
