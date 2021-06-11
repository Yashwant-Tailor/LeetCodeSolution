// cover the boundary cases 
// think about the combination parity 
// like n->even,m->even
// n->odd,m->even
// n->even,m->odd
// n->odd,m->odd
// see the pattern and look at the code
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int n  = matrix.size() , m = matrix[0].size() ;
        vector<int>ans ;
        for(int Ring = 0 ; Ring < min(n, m)/2 ; Ring++){
            for(int j = Ring ; j <= m - 1 - Ring ; j++){
                ans.push_back(matrix[Ring][j]) ; 
            }
            for(int i = Ring + 1 ; i <= n-1-Ring ; i++){
                ans.push_back(matrix[i][m - 1 - Ring]) ; 
            }
            for(int j = m - 1 - Ring - 1 ; j >= Ring ; j--){
                ans.push_back(matrix[n-1-Ring][j]) ; 
            }
            for(int i = n -1 -Ring -1 ; i > Ring ; i--){
                ans.push_back(matrix[i][Ring]) ; 
            }
        }
        if(m > n && n%2){
            for(int j = min(n , m)/2 ; j <= m - 1 - min(n , m)/2 ; j++){
                ans.push_back(matrix[min(n , m)/2][j]) ; 
            }
            
        }
        else if(m < n && m%2){
            for(int i = min(n , m)/2 ; i <= n -1 - min(n , m)/2  ; i++){
                ans.push_back(matrix[i][min(n , m)/2]) ; 
            }
        }
        else if(m == n && n%2){
            ans.push_back(matrix[n/2][n/2]);
        }
        return ans  ; 
    }
};
