// in next permutation every thing will same if we start comparing from left 
// only one index (let say i) will differ and after that everything will be in ascending order
// on the index where the permutations differ will contain next greater element which we can take from the ( i+1 to nums.size())
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size() == 1){
            return ; 
        }
        int i = nums.size() - 1 ; 
        while(i > 0){
            if(nums[i] <= nums[i-1]){
                i--;
            }
            else{
                break ; 
            }
        }
        i--;
        if(i == -1){
            for(int i = 0 ; i < (int)nums.size() / 2 ; i++){
                swap(nums[i] , nums[(int)nums.size() -1 - i ]) ; 
            }
        }
        else{
            // in next permutation we just need to find the element just greater than nums[i] from i+1 to num.size()
            // and swap that element with nums[i] ( if we have more than one occurance of that element than we will swap nums[i] with the right most one)
            int j = i+1  ; 
            int mi = nums[j]  , justGreInd = j ; 
            while(j < nums.size() && nums[j] > nums[i]){
                if(nums[j] <= mi){
                    justGreInd = j ;
                    mi = nums[j] ; 
                }
                j++;
            }
            swap(nums[justGreInd] , nums[i]) ; 
            for(int k = 0 ; k < (nums.size() - i -1 )/2 ; k++){
                swap(nums[i+1+k] , nums[nums.size() -1 + - k]) ;
            }
        }
        return  ;
    }
};