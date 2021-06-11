// hint : sort according the left end 
// start with one interval and find out all intervals which can merge with current interval with the help of right end of an interval
// see solution carefully
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin() , intervals.end() , [](const vector<int>&a , const vector<int>&b){
            return a[0] < b[0] ; 
        }) ;
        vector<vector<int>>ans;
        int i = 0 , n = intervals.size() ; 
        while(i < n){
            int leftend = intervals[i][0] ; 
            int rightend = intervals[i][1] ; 
            while(i < n && intervals[i][0] <= rightend){
                rightend = max(rightend , intervals[i][1]) ; 
                i++ ; 
            }
            vector<int>interval ; 
            interval.push_back(leftend) ; interval.push_back(rightend) ;
            ans.push_back(interval) ;
        }
        return ans ; 
    }
};
