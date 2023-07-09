/*
simple DP problem 
*/
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int sz = strs.size() ; 
        vector<vector<int>>count(sz , vector<int>(2 , 0)) ; 
        for(int i = 0 ; i < sz ; i++){
            for(int j = 0 ; j < strs[i].size() ; j++){
                count[i][0] += strs[i][j] == '0' ? 1 : 0 ; 
                count[i][1] += strs[i][j] == '1' ? 1 : 0 ; 
            }
        }
        vector<vector<int>>DP(n+1 , vector<int>(m+1 , 0)) ; 
        for(int k = 0 ; k < sz ; k++){
            for(int i = n ; i  >= 0 ; i--){
                for(int j = m ; j >= 0 ; j--){
                    if(k == 0){
                       if(count[k][0] <= j && count[k][1] <= i){
                            DP[i][j] = 1 ; 
                        } 
                    }
                    else{
                        if(i-count[k][1] >= 0 && j - count[k][0]>=0){
                            DP[i][j] = max(DP[i][j] , DP[i-count[k][1]][j - count[k][0]] + 1) ;
                        }
                    }
                }
            }
            // cout<<"k = "<<k<<endl;
            // for(int i = 0 ; i <= n ; i++){
            //     for(int j = 0 ; j <= m ; j++){
            //         cout<<DP[i][j]<<" ";
            //     }
            //     cout<<endl ;
            // }
            // cout<<endl;
        }
        return DP[n][m] ; 
    }
};
