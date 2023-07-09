// try to think the solution using marking
// we can use the first row and first column for marking
// if we need to set the entire to zero then for marking we will use the first cell of that row ( set it to zero)
// corner case : if you have to set the first row or column to zero then do it in the last 
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size()   , m = matrix[0].size() ; 
        bool is00r = false , is00c = false; 
        for(int i = 0 ; i < n ; i++){
            bool isZero = false ; 
            for(int j = 0 ; j < m ; j++){
                isZero |= (matrix[i][j] == 0) ;
                if(matrix[i][j] == 0){
                    if(j == 0){
                        is00c = true ;
                    }
                    matrix[0][j] = 0 ;
                }
            }
            
            if(isZero){
                if(i == 0 ){
                    is00r = true ;
                }
                matrix[i][0] = 0 ; 
            }
        }
       
        for(int i =  1  ; i < n ; i++){
            if(matrix[i][0] == 0){
                for(int j = 0 ; j < m ; j++){
                    matrix[i][j] =  0 ;
                }
            }
        }
        for(int j = 1 ; j < m; j++){
            if(matrix[0][j] == 0){
                for(int i = 0 ; i < n ; i++){
                    matrix[i][j] = 0 ; 
                }
            }
        }
        if(is00r){
            for(int j = 0 ; j < m ; j++){
                matrix[0][j] = 0 ;
            }
        }
        if(is00c){
            for(int i = 0 ; i < n ; i++){
                matrix[i][0] = 0  ;
            }
        }
        return ; 
    }
};
