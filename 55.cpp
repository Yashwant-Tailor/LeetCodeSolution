// maintain the maximum reachable index and then try to find out the index which can increase the reachable index from currIndex to reachable Index
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reachableIndex = 0 ; 
        int i = 0 ; 
        while(reachableIndex < nums.size() && i <= reachableIndex){
            int stepCanTake = i + nums[i]  ;
            reachableIndex = max(reachableIndex , stepCanTake) ; 
            i++ ; 
        }
        if(reachableIndex >= nums.size()-1){
            return true ;
        }
        return false ;
    }
};
