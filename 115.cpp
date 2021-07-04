/*
answer will overflow so somebody has to use modulo operator (mod  = INT_MAX , I saw in some accepted solution)
simple DP problem .
*/
class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size() , m = t.size() ; 
        long long int mod = INT_MAX ; 
        vector<vector<long long int>>DP(m+1 , vector<long long int>(n+1 , 0)) ; 
        //DP[i][j] = count of subsequence length i (it is prefix of t of length i) which we can be formed from the prefix of length j (this prefix will be from s)  .
        for(int j = 0 ; j <= n ; j++){
            DP[0][j] = 1 ;
        }
        for(int i = 1 ; i <= m ; i++){
            for(int j = 1 ; j <= n ; j++){
                DP[i][j] += DP[i][j-1] ;
                DP[i][j] %= mod ;
                if(t[i-1] == s[j-1]){
                    DP[i][j] += DP[i-1][j-1] ; 
                    DP[i][j] %= mod ; 
                }
            }
        }
        
        return (int)DP[m][n]; 
    }
};
