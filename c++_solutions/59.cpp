// same as spiral even easy I would say
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>>mat(n , vector<int>(n)) ; 
        int currElement = 1 ; 
        for(int Ring = 0 ; Ring < n/2 ; Ring++){
            for(int j = Ring ; j <= n-1-Ring ; j++){
                mat[Ring][j] = currElement ;
                currElement++ ;
            }
            for(int i = Ring+1 ; i <= n-1-Ring ; i++){
                mat[i][n-1-Ring] = currElement ; 
                currElement++ ; 
            }
            for(int j = n-1-Ring-1 ; j >= Ring ; j--){
                mat[n-1-Ring][j] = currElement ; 
                currElement++ ; 
            }
            for(int i = n-1-Ring-1 ; i > Ring ; i--){
                mat[i][Ring] = currElement  ;
                currElement++ ; 
            }
        }
        if(n%2){
            mat[n/2][n/2] = currElement ; 
        }
        return mat ; 
    }
};
