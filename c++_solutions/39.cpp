// simple recursion 
// points to remember
// 1. to avoid the duplication of combination use all occurance of an element continously , don't start iterating from any previous index
// 2. remember to pop the element so that duplication not happen
// 3. closely look at the for loop in recursion ( u will get everything)
class Solution {
public:
    void FindAns(vector<int>& c , int t , int ind , vector<int>currSum , vector<vector<int>> & ans){
        if(ind == c.size() && t!=0){
            return  ; 
        }
        if(t == 0){
            ans.push_back(currSum)  ;
            return ;
        }
        for(int i = ind ; i < c.size() ; i++){
            int elCount = t / c[i] ; 
            int temp_target = t ; 
            while(elCount != 0){
                currSum.push_back(c[i]) ; 
                temp_target -= c[i] ; 
                FindAns(c , temp_target , i+1 , currSum , ans) ; 
                elCount-- ; 
            }
            elCount = t / c[i] ; 
            while(elCount != 0){
                currSum.pop_back() ; 
                elCount--;
            }
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>ans ; 
        vector<int>currSum ;
        int ind = 0 ;
        FindAns(candidates , target , ind , currSum  ,  ans) ; 
        return ans ; 
    }
};