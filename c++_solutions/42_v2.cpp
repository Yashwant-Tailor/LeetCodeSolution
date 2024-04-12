class Solution {
public:
    int trap(vector<int>& height) {
        int seen_max_height = -1 ; 
        vector<int> L ,R;
        for(auto h : height){
            seen_max_height = max(h , seen_max_height) ;
            L.push_back(seen_max_height) ;
        }
        seen_max_height = -1 ;
        for(int i = height.size()-1 ; i >= 0;i--){
            seen_max_height = max(height[i] , seen_max_height) ;
            R.push_back(seen_max_height) ;
        }
        reverse(R.begin() , R.end()) ; 
        int water_trapped = 0 ;
        for(int i = 0 ;i < height.size() ; i++){
            // cout<<"h: "<<height[i]<<" L: "<<L[i]<<" R: "<<R[i]<<endl;
            water_trapped += abs(height[i] - min(L[i],R[i]));
        }
        return water_trapped ;
    }
};
