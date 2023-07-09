//approx. same as combination problem 39

class Solution {
public:
    void FindAns(vector<int> & a , vector<int>&b , int t , int ind , vector<int>com , vector<vector<int>>&ans){
        
        if(ind == a.size() && t!=0){
            return  ; 
        }
        if(t < 0){
            return  ; 
        }
        if(t == 0){
            ans.push_back(com) ; 
            return  ; 
        }
        for(int i = ind  ; i < a.size() ; i++){
            int temp_target = t ; 
             for(int j = 1 ; j <= b[i]  ; j++){
                 com.push_back(a[i]) ; 
                 temp_target -= a[i] ; 
                 FindAns(a , b , temp_target , i+1 , com , ans) ; 
             }
            for(int j =1 ;j <= b[i] ; j++){
                com.pop_back() ; 
            }
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin() , candidates.end()) ; 
        vector<int>a , b ; 
        for(size_t i = 0 ; i < candidates.size() ; ){
            int el = candidates[i] ; 
            int count = 0 ; 
            for(;i<candidates.size() && el == candidates[i] ; i++){
                count++ ; 
            }
            a.push_back(el) ; 
            b.push_back(count) ; 
        }
        vector<vector<int>>ans ; 
        vector<int>com ; 
        int ind = 0 ; 
        FindAns(a , b , target , ind , com , ans) ; 
        return ans ; 
    }
};
