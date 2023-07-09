/*
apart from recurssion we can use 
*/
class Solution {
public:
    bool find_ans(vector<int>&nums , int l , int r , int s1 , int s2 , int turn1){
        if(l == r){
            if(turn1){
                return s1 + nums[l] >= s2 ; 
            }
            else{
                return s1 >= s2+nums[l] ; 
            }
        }
        else{
            if(turn1){
                return find_ans(nums , l+1 , r , s1+nums[l] , s2 ,false)|find_ans(nums,l , r-1 ,s1+nums[r] , s2 , false) ; 
            }
            else{
                return find_ans(nums , l+1 ,r , s1 , s2+nums[l] , true)&find_ans(nums,l , r-1 , s1 , s2+nums[r] , true);
            }
        }
    }
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size() ; 
        return find_ans(nums  , 0 , n-1 , 0 , 0 , true) ;
    }
};
