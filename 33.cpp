// try to discard an interval if a[mid] is not equal to target
// to discard an interval first see what relation we have with the boundary element 
// and then compare target with a[mid] and boundary element and discard the appropriate interval
class Solution {
public:
    int search(vector<int>& a, int target) {
        int l = 0 , r = a.size() -1  ; 
        while(r >=  l){
            int mid = (r+l)/2 ; 
            if(a[mid] == target){
                return mid ; 
            }
            if(a[mid] >= a[l]){
                if(a[mid]>= target && a[l] <= target){
                    r = mid -1  ;
                }
                else{
                    l = mid + 1 ;
                }
            }
            else{
                if(a[mid] <= target && a[r] >= target){
                    l = mid+1 ; 
                }
                else{
                    r = mid -1 ;
                }
            }
        }
        return -1 ;
    }
};