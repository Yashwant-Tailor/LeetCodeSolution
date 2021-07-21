/*
after sorting the answer is very clear just remeber the method so that in future you don't waste your time 
on thinking the solution which you already know .
*/
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        int n = nums.size() ; 
        if(n == 0){
            return 0 ; 
        }
        sort(nums.begin() , nums.end());
        int ans = 0 ; 
        int i = 0 ; 
        int change_to = nums[i] ;
        while(i < n ){
            if(nums[i] <= change_to){
                ans += abs(change_to - nums[i]) ; 
                i++;change_to++ ;
            }
            else{
                change_to = nums[i] ;
            }
        }
        return ans ; 
    }
};
