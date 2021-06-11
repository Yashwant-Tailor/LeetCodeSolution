// simple , see below solution
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix[0].size() ;
        int OperationForRing = n - 1  ;
        for(int Ring = 0 ; Ring < n/2 ; Ring++){
            int UpperRow = Ring , LowerRow = n - 1 - Ring ;
            int LeftColumn =  Ring , RightColumn = n - 1 - Ring ; 
            int itr_Lower_Left = n - 1 - Ring , itr_Upper_Right = Ring ; 
            for(int  op  = 0 ; op < OperationForRing ; op++){
                swap(matrix[UpperRow][itr_Upper_Right] , matrix[itr_Lower_Left][LeftColumn]) ; 
                swap(matrix[itr_Lower_Left][LeftColumn] , matrix[LowerRow][itr_Lower_Left]) ; 
                swap(matrix[LowerRow][itr_Lower_Left] , matrix[itr_Upper_Right][RightColumn]) ; 
                itr_Lower_Left--;
                itr_Upper_Right++ ;
            }
            OperationForRing  -= 2;
        }
        return ; 
    }
};
