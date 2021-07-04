/*
simple solution 
two state for DP
state 1 : rob the current house
state 2 : don't rob the current house
look at the code for the transition of the this states
*/
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size() ;
        int previous_rob = 0 , previous_not_rob = 0 ; 
        int current_rob = nums[0] , current_not_rob = 0 ; 
        for(int i = 0 ; i < n ; i++){
            current_rob = nums[i] + previous_not_rob ; 
            current_not_rob = max(previous_not_rob , previous_rob) ; 
            previous_rob = current_rob ; 
            previous_not_rob = current_not_rob ; 
        }
        return max(current_rob , current_not_rob) ; 
    }
};
