// two pointer simple
class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0 ; 
        int i = 0 , j = height.size() -1 ; 
        while( i < j){
            int mi = min(height[i]   , height[j]) ; 
            ans  = max(ans , (j-i)* mi) ; 
            if(mi == height[i]){
                i++  ;
            }
            else{
                j--;
            }
        }
        return ans ; 
    }
};
