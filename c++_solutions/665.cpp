/*
if somewhere in the array at index i the condition nums[i]<=nums[i+1] (i from 1 to n-1)
doesn't hold then we have only two option either change num[i] or change num[i+1] .
we only allowed to change one element so find an element where this condition doesn't hold and then
check for the above two possibilities , if any of them is possible then we say that we can make the
array non decreasing.
*/
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        bool ans1  = true  , ans2 = true ; 
        for(int i = 0 ; i < (int)nums.size() - 1 ; i++){
            if(nums[i] > nums[i+1]){
                int i1 = i+1 , i2 = i+2 ; 
                if(i1-2>=0){
                    ans1 &= nums[i1] >= nums[i1-2] ; 
                }
                if(i2<nums.size()){
                    ans2 &= nums[i2] >= nums[i2-2] ; 
                }
                while(i1<nums.size() -1){
                    ans1 &= nums[i1]<=nums[i1+1] ;i1++ ;
                }
                while(i2+1<nums.size()){
                    ans2 &= nums[i2] <= nums[i2+1] ;i2++;
                }
                break;
            }
        }
        return ans1|ans2;
    }
};
