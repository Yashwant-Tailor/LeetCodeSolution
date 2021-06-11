// hint : what ever amount of water will trapped at is only depend on length of the current bar and bar with maximum height in right and bar with maximum height in left
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size() ; 
        if(n < 3){
            return 0 ; 
        }
        int s = height[0 ] ;
        vector<int>L(n) , R(n) ; 
        
        for(int i = 0; i < n ;i++){
            s = max(s , height[i]) ; 
            L[i] = s ; 
        }
        int s1 = height[n-1] ;
        for(int i = n-1 ; i>=0 ; i--){
            s1 = max(s1 , height[i])  ;
            R[i] = s1 ; 
        }
        int water = 0 ; 
        for(int i = 0 ; i <n ; i++){
            water += min(L[i] , R[i])  - height[i]; 
        }
        return water ; 
    }
};
