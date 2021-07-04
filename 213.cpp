/*
This problem is same as House Robber I
can make it look like same as above by considering three cases
Case 1: rob house 1 but don't rob house n ( it simply House Robber I problem with i in range (1 to n-1))
Case 2: rob house n but don't rob house 1 ( it simply House Robber I problem with i in range( 2 to n))
Case 3: don't rob house 1 and n (it simply House Robber I problem with i in range(2 to n-1))
return the maximum of this three cases
*/
class Solution {
public:
    int rob(vector<int>& nums) {
        
        int n = nums.size() , ans1 = 0 , current_rob = 0 , current_not_rob = 0 , previous_rob = 0 , previous_not_rob = 0 ; 
        if(n == 1){
            return nums[0] ;
        }
        for(int i = 0 ; i < n-1 ; i++){
            current_rob = nums[i] + previous_not_rob ; 
            current_not_rob = max(previous_rob , previous_not_rob) ;
            previous_rob = current_rob ; 
            previous_not_rob = current_not_rob ; 
        }
        ans1 = max(current_rob  , current_not_rob) ;
        int ans2 = 0 ;
        current_rob = 0 , current_not_rob = 0 , previous_rob = 0 , previous_not_rob = 0 ; 
        for(int i = 1 ; i  < n ;i++){
            current_rob = nums[i] + previous_not_rob ; 
            current_not_rob = max(previous_rob , previous_not_rob) ;
            previous_rob = current_rob ; 
            previous_not_rob = current_not_rob ; 
        }
        ans2 = max(current_rob  , current_not_rob) ;
        int ans3 = 0 ;
        current_rob = 0 , current_not_rob = 0 , previous_rob = 0 , previous_not_rob = 0 ; 
        for(int i = 1 ; i  < n -1;i++){
            current_rob = nums[i] + previous_not_rob ; 
            current_not_rob = max(previous_rob , previous_not_rob) ;
            previous_rob = current_rob ; 
            previous_not_rob = current_not_rob ; 
        }
        ans3 = max(current_rob  , current_not_rob) ;
        return max(ans1 , max(ans2 , ans3)) ; 
    }
};
