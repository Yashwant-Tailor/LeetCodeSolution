/*
define an prefix array such that prefix[i] = count1 - count0 ; 
between two index the count of 0 and 1 will be same if 
prefix[i] - prefix[j] = 0 ; because (prefix[i] = prefix[j] + (count1 - count0 in between i and j))
and because count1 = count0 in between i and j
so prefix[i] = prefix[j] 

O(n) solution is to maintain an hashmap and store the first index for a particular sum 

*/
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size() ; 
        unordered_map<int,int>ind ;
        int su = 0; 
        ind[0] = -1;
        int ans = 0 ; 
        for(int i = 0 ; i < n ;i++){
            su += nums[i] ? 1 : -1 ; 
            if(ind.find(su) != ind.end()){
                ans = max(ans , i - ind[su]);
            }
            else{
            ind[su] = i ; 
            }
        }
        return ans ; 
    }
};
