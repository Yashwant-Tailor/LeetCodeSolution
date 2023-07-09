/*
binary search and use the below predicate to discard the particular range 
see the below solution 
*/
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0  , r = nums.size() ; 
        while(l < r){
            int mid = (l+r)/2 ; 
            if(mid+1<r && nums[mid] == nums[mid+1]){
                mid++;
                if((mid-l+1)%2){
                    r = mid-1 ; 
                }
                else{
                    l = mid+1 ; 
                }
            }
            else if(mid -1 >= l && nums[mid] == nums[mid-1]){
                if((mid-l+1)%2){
                    r = mid-1 ; 
                }
                else{
                    l = mid+1 ; 
                }
            }
            else{
                return nums[mid] ; 
            }
        }
        return nums[l] ; 
    }
};
