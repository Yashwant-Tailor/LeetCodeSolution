// remember the corner case 
// case 1. when the lenght of intervals is zero
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int i = 0 , n = (int)intervals.size() ; 
        
        vector<vector<int>>ans ; 
        if(n == 0){
            ans.push_back(newInterval) ; 
            return ans ; 
        }
        while(i < n){
            if(newInterval[0] < intervals[i][0] ){
                int leftend = newInterval[0] ; 
                int rightend = newInterval[1] ; 
                while(i < n && rightend >= intervals[i][0] ){
                    rightend = max(rightend , intervals[i][1]) ; 
                    i++ ;
                }
                vector<int>temp ; 
                temp.push_back(leftend) ; temp.push_back(rightend) ; 
                ans.push_back(temp) ; 
                while(i <n){
                    ans.push_back(intervals[i]) ; 
                    i++ ; 
                }
            }
            else if(intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[0]){
                int leftend = intervals[i][0] ; 
                int rightend = max(newInterval[1] , intervals[i][1]) ; 
                while(i <n && rightend >= intervals[i][0]){
                    rightend = max(rightend  , intervals[i][1]) ; 
                    i++ ;
                }
                vector<int>temp ; 
                temp.push_back(leftend) ; temp.push_back(rightend) ; 
                ans.push_back(temp) ; 
                while(i <n){
                    ans.push_back(intervals[i]) ; 
                    i++ ; 
                }
            }
            else{
                ans.push_back(intervals[i]) ; 
                i++ ;
            }
        }
        if(intervals[n-1][1] < newInterval[0]){
            ans.push_back(newInterval) ;
        }
        return ans ; 
    }
};
