/*
do simple dfs and mark every cell for which the water of cell can come to pacific ocean 
do the same thing for atlantic and then just check the cell which is marked for both the oceans
*/
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& H) {
        int n = H.size() , m = H[0].size() ; 
        vector<vector<bool>>pac(n , vector<bool>(m , false)) ; 
        vector<vector<bool>>vis(n , vector<bool>(m , false)) ; 
        queue<pair<int,int>>q ; 
        for(int i = 0 ; i < n ;i++){
            q.push({i , 0}) ; 
            pac[i][0] = true ; vis[i][0] = true ;
        }
        for(int j = 0 ; j < m ; j++){
            q.push({0 , j}) ; 
            pac[0][j] = true ; 
            vis[0][j] = true ;
        }
        while(!q.empty()){
            int sz = q.size() ; 
            while(sz--){
                pair<int,int>node = q.front() ; q.pop() ; 
                int i = node.first  , j = node.second ; 
                if(i+1 < n && !vis[i+1][j] && H[i][j]<=H[i+1][j]){
                    vis[i+1][j] = true ;
                    pac[i+1][j ] =true ; 
                    q.push({i+1 , j}) ; 
                }
                if(j+1<m && !vis[i][j+1] && H[i][j]<= H[i][j+1]){
                    vis[i][j+1] = true ; 
                    pac[i][j+1] = true ; 
                    q.push({i , j+1}) ; 
                }
                if(i-1>=0 && !vis[i-1][j] && H[i-1][j] >= H[i][j]){
                    vis[i-1][j] = true ; 
                    pac[i-1][j] = true ; 
                    q.push({i-1 , j}) ; 
                }
                if(j-1>=0 && !vis[i][j-1] && H[i][j-1]>=H[i][j]){
                    vis[i][j-1] = true ; 
                    pac[i][j-1] = true ; 
                    q.push({i , j-1}) ; 
                }
            }
        }
        for(int i = 0  ; i < n ;i++){
            for(int j = 0 ; j < m ;j++){
                vis[i][j] = false ; 
            }
        }
        queue<pair<int,int>>q1 ; 
        vector<vector<bool>>atl(n , vector<bool>(m , false)) ; 
        for(int i = 0 ; i < n ; i++){
            atl[i][m-1] = true ; vis[i][m-1] = true ; 
            q1.push({i , m-1}) ; 
        }
        for(int j = 0  ; j < m ;j++){
            atl[n-1][j] = true ; vis[n-1][j] = true ; 
            q1.push({n-1 , j}) ; 
        }
        while(!q1.empty()){
            int sz  = q1.size() ; 
            while(sz--){
                pair<int,int>node = q1.front() ; q1.pop() ; 
                int i = node.first , j = node.second ; 
                if(i+1 < n && !vis[i+1][j] && H[i][j]<=H[i+1][j]){
                    vis[i+1][j] = true ;
                    atl[i+1][j ] =true ; 
                    q1.push({i+1 , j}) ; 
                }
                if(j+1<m && !vis[i][j+1] && H[i][j]<= H[i][j+1]){
                    vis[i][j+1] = true ; 
                    atl[i][j+1] = true ; 
                    q1.push({i , j+1}) ; 
                }
                if(i-1>=0 && !vis[i-1][j] && H[i-1][j] >= H[i][j]){
                    vis[i-1][j] = true ; 
                    atl[i-1][j] = true ; 
                    q1.push({i-1 , j}) ; 
                }
                if(j-1>=0 && !vis[i][j-1] && H[i][j-1]>=H[i][j]){
                    vis[i][j-1] = true ; 
                    atl[i][j-1] = true ; 
                    q1.push({i , j-1}) ; 
                }
            }
        }
        vector<vector<int>>ans ; 
        for(int i = 0 ; i < n ;i++){
            for(int j = 0 ; j < m ; j++){
                if(pac[i][j] == true && atl[i][j] == true){
                    vector<int>temp ; temp.push_back(i) ; temp.push_back(j) ; 
                    ans.push_back(temp) ; 
                }
            }
        }
        return ans ; 
    }
};
