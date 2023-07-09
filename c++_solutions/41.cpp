// hint : try to mark the element in range (1 to n)
// hint : for marking we can use the array index 
// hint : whenever we find that a number is not on correct position we can place that number on correct postion by swapping the element on current position with the element on the position denoted by the current element (so in the end we will have that number on its correct position)
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size() ; 
        for(size_t i = 0 ; i < nums.size() ; i++){
            while(nums[i] >= 1 && nums[i] <= n && nums[i] != nums[nums[i]-1]){
                swap(nums[i] , nums[nums[i]-1]) ;
            }
        }
        for(int i  = 0 ; i < n; i++){
            if(nums[i]  != i+1){
                return i+1 ; 
            }
        }
        return n+1 ;
    }
};
