class EarlySecond {
    private :
        vector<int> & nums ; 
        vector<int>& ci ; 
        bool is_pos(size_t mid) ;
    public : 
        EarlySecond(vector<int>&nums,vector<int>&changeIndices): nums(nums),ci(changeIndices) {}
        int find_sec();
};
int EarlySecond::find_sec(){
    size_t l = 1 , r = ci.size() ; 
    while (l < r){
        size_t mid = l + (r-l)/2 ; 
        if (is_pos(mid)){
            r = mid; 
        } 
        else {
            l = mid+1 ;
        }
    }
    return is_pos(l) ? l : -1 ;
}
bool EarlySecond::is_pos(size_t mid){
    vector<int>ind(nums.size() , -1);
    for (size_t i = 0  ; i < mid ; ++i){
        int curr_ind = ci[i] - 1 ;
        ind[curr_ind] = i ; 
    }
    vector<bool>is_last(ci.size() , false);
    for(size_t i = 0 ; i < ind.size() ; ++i){
        if (ind[i] != -1){
            is_last[ind[i]] = true ;
        }
    }
    int sum_marked = 0 ;
    int cnt_marked = 0;
    for (size_t i = 0 ; i < is_last.size() ;++i){
        if (is_last[i]){
            if(i+1-cnt_marked-sum_marked>=nums[ci[i]-1]+1){
                cnt_marked++;
                sum_marked += nums[ci[i]-1] ;
            }
            else{
                return false;
            }
        }
    }
    return cnt_marked == nums.size() ? true : false ;
}
class Solution {
    
public:
    int earliestSecondToMarkIndices(vector<int>& nums, vector<int>& changeIndices) {
        EarlySecond es(nums,changeIndices);
        return es.find_sec() ;
    }
};
