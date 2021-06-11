// same as 3sum question (problem no. 11)
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin() , nums.end()) ; 
        int ans = nums[0] + nums[1] + nums[2] ; 
        for(int i = 0 ; i <nums.size() -2 ; i++){
            int j  = i + 1 , k = nums.size() -1 ; 
            while(j < k){
                if(abs(ans - target) > abs(nums[i] + nums[j] + nums[k]  - target)){
                    ans  = nums[i] + nums[j] + nums[k] ; 
                }
                if(nums[i] + nums[j] + nums[k] > target){
                    k-- ; 
                }
                else{
                    j++ ; 
                }
            }
        }
        return ans ; 
    }
};