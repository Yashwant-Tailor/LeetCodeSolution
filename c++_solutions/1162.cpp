/*
simple bfs 
*/
class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int n = grid.size()  ; 
        vector<vector<int>>dis(n , vector<int>(n , n+n+1)) ; 
        queue<pair<int,int>>q ; 
        vector<vector<bool>>vis(n , vector<bool>(n , false)) ; 
        int count = 0 ; 
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < n ; j++){
                if(grid[i][j]){
                    q.push({i , j}) ; 
                    vis[i][j] = true ; 
                    dis[i][j] = 0 ; 
                    count++;
                }
            }
        }
        if(count == 0 || count == n*n){
            return -1 ;
        }
        while(!q.empty()){
            int sz = q.size() ; 
            while(sz--){
                pair<int,int>node = q.front() ; 
                int i = node.first , j = node.second ; q.pop() ;
                if(i-1>=0 && !vis[i-1][j]){
                    q.push({i-1 , j}) ; 
                    vis[i-1][j] = true ; 
                    dis[i-1][j] = dis[i][j] + 1 ; 
                }
                if(j-1>=0 && !vis[i][j-1]){
                    q.push({i , j-1}) ; 
                    vis[i][j-1] = true ; 
                    dis[i][j-1] = dis[i][j] + 1 ;
                }
                if(i+1<n && !vis[i+1][j]){
                    q.push({i+1 , j}) ; 
                    vis[i+1][j] = true ; 
                    dis[i+1][j] =dis[i][j]+ 1 ;
                }
                if(j+1<n && !vis[i][j+1]){
                    q.push({i , j+1}) ; 
                    vis[i][j+1] = true ; 
                    dis[i][j+1] = dis[i][j] + 1 ;
                }
            }
        }
        int ans = 0 ; 
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j  < n ;j++){
                ans = max(ans , dis[i][j]) ; 
            }
        }
        return ans ; 
    }
};
