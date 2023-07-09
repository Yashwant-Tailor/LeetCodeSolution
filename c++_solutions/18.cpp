// same as 3sum tirplets
// after sorting
// case1: all the four number(nums[a] , nums[b] , nums[c] , nums[d]) are different
// case2: (nums[a] , nums[b] , nums[c] , nums[c])
// case3: (nums[a] , nums[b] , nums[b] , nums[c]) 
// case4: (nums[a] , nums[b] , nums[b] , nums[b])
// case5: (nums[a]  , nums[a] , nums[b] , nums[c]) 
// case6: (nums[a] , nums[a] , nums[b] , nums[b])
// case7: (nums[a] , nums[a]  , nums[a] , nums[b])
// case8 :(numa[a] , nums[a] , nums[a] , nums[a]) 
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin() , nums.end()) ; 
        vector<int>a , b ; 
        for(int i = 0 ; i < nums.size() ; ){
            int el = nums[i] ; 
            a.push_back(el) ; 
            int count = 0 ; 
            for(; i < nums.size() && el == nums[i]; i++){
                count++  ;
            }
            b.push_back(count) ;
        }
        vector<vector<int>>ans ; 
        for(int i = 0 ; i < (int)a.size() - 3 ; i++){
            for(int j = i+1 ; j < (int)a.size() -2 ; j++){
                int k = j+1 , l = (int)a.size() -1 ; 
                while(k < l){
                    if(a[i] + a[j] + a[k] + a[l] == target){
                        vector<int>temp ; 
                        temp.push_back(a[i]) ; temp.push_back(a[j]) ; temp.push_back(a[k]) ; temp.push_back(a[l]) ;
                        ans.push_back(temp) ; 
                    }
                    if(a[i] + a[j] + a[k] + a[l] < target){
                        k++ ; 
                    }
                    else{
                        l--;
                    }
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() - 2 ; i++){
            for(int j = i+1; j < (int)a.size() - 1 ; j++){
                for(int k  = j+1 ; k < (int)a.size() ; k++){
                    if(b[j] > 1 && a[i] + 2*a[j] + a[k] == target){
                        vector<int>temp ; 
                        temp.push_back(a[i]) ; temp.push_back(a[j]) ; temp.push_back(a[j]) ; temp.push_back(a[k]) ; 
                        ans.push_back(temp) ; 
                    }
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() - 2 ; i++){
            for(int j = i+1; j < (int)a.size() - 1 ; j++){
                for(int k  = j+1 ; k < (int)a.size() ; k++){
                    if(b[k] > 1 && a[i] + a[j] + 2*a[k] == target){
                        vector<int>temp ; 
                        temp.push_back(a[i]) ; temp.push_back(a[j]) ; temp.push_back(a[k]) ; temp.push_back(a[k]) ; 
                        ans.push_back(temp) ; 
                    }
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() - 2 ; i++){
            for(int j = i+1; j < (int)a.size() - 1 ; j++){
                for(int k  = j+1 ; k < (int)a.size() ; k++){
                    if(b[i] > 1 && 2*a[i] + a[j] + a[k] == target){
                        vector<int>temp ; 
                        temp.push_back(a[i]) ; temp.push_back(a[i]) ; temp.push_back(a[j]) ; temp.push_back(a[k]) ; 
                        ans.push_back(temp) ; 
                    }
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() -1  ; i++){
            for(int j = i+1 ; j<(int)a.size() ; j++){
                if(b[i] > 1 && b[j]>1 && 2*a[i] + 2*a[j] == target){
                    vector<int>temp ; 
                    temp.push_back(a[i]); temp.push_back(a[i]) ; temp.push_back(a[j]) ;temp.push_back(a[j]) ; 
                    ans.push_back(temp) ;
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() -1  ; i++){
            for(int j = i+1 ; j<(int)a.size(); j++){
                if(b[j] > 2 && 3*a[j] + a[i] == target){
                    vector<int>temp ; 
                    temp.push_back(a[i]); temp.push_back(a[j]) ; temp.push_back(a[j]) ;temp.push_back(a[j]) ; 
                    ans.push_back(temp) ;
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() -1  ; i++){
            for(int j = i+1 ; j<(int)a.size() ; j++){
                if(b[i] > 2 && 3*a[i] + a[j] == target){
                    vector<int>temp ; 
                    temp.push_back(a[i]); temp.push_back(a[i]) ; temp.push_back(a[i]) ;temp.push_back(a[j]) ; 
                    ans.push_back(temp) ;
                }
            }
        }
        for(int i = 0 ; i < (int)a.size() ; i++){
                if(b[i] > 3 && 4*a[i] == target){
                    vector<int>temp ; 
                    temp.push_back(a[i]); temp.push_back(a[i]) ; temp.push_back(a[i]) ;temp.push_back(a[i]) ; 
                    ans.push_back(temp) ;
                }
        }
        return ans ; 
    }
};