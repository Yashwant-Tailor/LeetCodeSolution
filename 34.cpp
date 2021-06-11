// one binary search for l and other one for r
class Solution {
public:
    vector<int> searchRange(vector<int>& a, int target) {
        int l = 0 , r = a.size() ; 
        while( l < r){
            int mid = (l+r)/2 ; 
            if(a[mid] >= target){
                r = mid ; 
            }
            else{
                l = mid+1 ; 
            }
        }
        vector<int>ans ; 
        if( r != a.size() and a[r] == target){
            ans.push_back(r) ; 
             l = 0 , r = a.size() ; 
            while( l < r){
                int mid = (l+r)/2 ; 
                if(a[mid] > target){
                    r = mid ; 
                }
                else{
                    l = mid+1 ; 
                }
            }
            ans.push_back(l-1) ; 
            return ans ; 
        }
        else{
            ans.push_back(-1) ; ans.push_back(-1) ;
            return ans ; 
        }
    }
};