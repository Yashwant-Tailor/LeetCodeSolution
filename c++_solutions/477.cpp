/*
calculate the bits wise contribution to the answer .
*/
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int n = nums.size() ; 
        vector<int>count1(32 , 0) , count0(32 ,0) ; 
        for(int i = 0 ; i < n ;i++){
            int j = 0 ; 
            while(nums[i]){
                if(nums[i] & 1){
                    count1[j]++;
                }
                else{
                    count0[j]++;
                }
                j++;
                nums[i] >>= 1 ;
            }
            while(j < 32){
                count0[j]++;j++;
            }
        }
        int ans = 0 ; 
        for(int i = 0 ; i < 32 ; i++){
            ans += count1[i] * count0[i] ; 
        }
        return ans ; 
    }
};
