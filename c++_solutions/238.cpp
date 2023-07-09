/*
divide in three case
case1 : when we have more than 1 zero ; in this case ans[i] = 0 
case2: when we have exactly 1 zero ; in this case ans[i] = 0 except an index i such that nums[i] = 0 , for this index we can calculate the answer in O(n) 
case3: when we don't have any zero ; in this case first calculate the totalProduct , ans[i] = totalProduct/nums[i]
*/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int count0  = 0 ; 
        int n = nums.size()  ;
        for(int i = 0 ; i < n ;i++){
            count0 += nums[i] == 0 ? 1 : 0 ; 
        }
        vector<int>ans ; 
        if(count0 > 1){
            for(int i = 0 ;i < n ;i++){
                ans.push_back(0) ; 
            }
        }
        else if(count0 == 1){
            int ansi = 1 ; 
            int ind = -1 ;
            for(int i = 0 ; i < n ; i++){
                if(nums[i]!=0){
                    ans.push_back(0) ; 
                    ansi *= nums[i] ;
                }
                else{
                    ind = i ; 
                    ans.push_back(0) ;
                }
            }
            ans[ind] = ansi ; 
        }
        else{
            int totalProduct = 1 ; 
            for(int i = 0 ; i < n ;i++){
                totalProduct *= nums[i] ;
            }
            for(int i = 0 ; i < n ;i++){
                ans.push_back(totalProduct/nums[i]) ; 
            }
        }
        return ans ;
    }
};
