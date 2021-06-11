// simple binary search
class Solution {
public:
    int searchInsert(vector<int>& a, int target) {
        int l = 0 , r = a.size() , mid ; 
        while( l < r){
            mid = (l+r)/2 ; 
            if(a[mid] > target){
                r = mid  ; 
            }
            else{
                l = mid+1  ;
            }
        }
        if(l -1 >= 0 && a[l-1] == target){
            return l-1 ; 
        }
        else{
            return l ; 
        }
    }
};