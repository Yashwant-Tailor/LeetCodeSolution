// simple DP
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if(obstacleGrid[0][0] == 1){
            return  0 ;
        }
        int n = obstacleGrid.size() , m = obstacleGrid[0].size() ;
        vector<vector<int>>DP(n , vector<int>(m   ,0)) ; 
        DP[0][0] = 1 ; 
        for(int i =  0 ; i <n ; i++){
            for(int j = 0 ; j <  m ; j++){
                if((i!=0 || j!=0) && obstacleGrid[i][j]!=1){
                    if(i-1>=0){
                        DP[i][j] += DP[i-1][j] ; 
                    }
                    if(j-1>=0){
                        DP[i][j] += DP[i][j-1] ; 
                    }
                }
            }
        }
        return DP[n-1][m-1] ; 
    }
};
