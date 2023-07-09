/*
Hint1 : for any cell find the height of 1's ( see the first for loop and its inner loop)
Hint2 : Now find the maximum horizontal length of 1's for a particular cell with a given height( think which cell can be included for a particular cell)
Solution of above hint2 : horizontally we will include every cell which has height of 1's (as we calculate in Hint1) greater than or equal to the height of current cell 
OR
stand at the current cell go to left find the first cell which has height of 1's less than current cell
then again stand at current cell go to right and find the cell which has height of 1's less than current cell
( This standard problem which can be solved in O(n) using stack )
*/

/*
Don't forget the corner case when we have n == 0
*/

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
       int n  = matrix.size() ; 
        if(n == 0){
            return  0 ; 
        }
        int m  = matrix[0].size() ; 
        int ans = 0 ; 
        vector<vector<int>>DP(n , vector<int>(m , 0)) ; 
        for(int i  = 0  ; i < n ; i++){
            for(int j = 0 ;  j < m ; j++){
                if(matrix[i][j] == '0'){
                    DP[i][j] = 0 ; 
                } 
                else if(i == 0){
                    DP[i][j] = 1 ; 
                }
                else{
                    DP[i][j]  += DP[i-1][j] + 1 ; 
                }
                ans = max(ans , DP[i][j]) ; 
            }
        }
        for(int i = 0 ; i < n ; i++){
            vector<int>L(m) , R(m) ; 
            stack<int>s ; 
            s.push(0) ;
            L[0] = 0 ; 
            for(int j = 1 ; j <  m ; j++){
                while(!s.empty() && DP[i][j] <= DP[i][s.top()]){
                    s.pop() ; 
                }
                if(s.empty()){
                    L[j] = 0 ; 
                }
                else{
                    L[j] = s.top() + 1 ; 
                }
                s.push(j) ; 
            }
            stack<int>s1 ;
            s1.push(m-1) ; 
            R[m-1] = m-1  ;
            for(int j = m-2 ; j>=0 ; j--){
                while(!s1.empty() && DP[i][j] <= DP[i][s1.top()]){
                    s1.pop() ; 
                }
                if(s1.empty()){
                    R[j] = m-1 ; 
                }
                else{
                    R[j] = s1.top() -1 ;
                }
                s1.push(j) ;
            }
            for(int j = 0 ; j < m ; j++){
                ans = max(ans , (R[j] - L[j] + 1) * DP[i][j]);
            }
        }
        return ans  ;
    }
};
