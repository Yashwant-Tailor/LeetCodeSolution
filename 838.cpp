/*
this solution uses the BFS to find the answer 
*/
class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size() ; 
        vector<char>finalState(n , '.') ; 
        vector<int>color(n , 0) ; 
        queue<int>q ; 
        for(int i = 0 ; i < n ; i++){
            if(dominoes[i] != '.'){
                q.push(i) ; 
                finalState[i] = dominoes[i] ; 
                color[i] = 2 ; 
            }
        }
        while(!q.empty()){
            int sz = q.size() ; 
            while(sz--){
                int ind = q.front() ; q.pop() ; 
                if(finalState[ind] == 'R' && ind+1<n){
                    if(color[ind+1] == 0){
                        q.push(ind+1) ; 
                        finalState[ind+1] = 'R'  ;
                        color[ind+1] = 1; 
                    }
                    else{
                        if(color[ind+1] == 1){
                            finalState[ind+1] = '.' ; 
                            color[ind] = 2 ; 
                        }
                    }
                }
                if(finalState[ind] == 'L' && ind-1>=0){
                    if(color[ind-1] == 0){
                        q.push(ind-1) ; 
                        color[ind-1] = 1 ; 
                        finalState[ind-1] = 'L' ; 
                    }
                    else{
                        if(color[ind-1] == 1){
                            color[ind-1] = 2; 
                            finalState[ind-1] = '.' ; 
                        }
                    }
                }
            }
            sz  = q.size() ; 
            while(sz--){
                int ind = q.front() ; q.pop() ; q.push(ind) ; 
                if(color[ind] == 1){
                    color[ind] = 2 ; 
                }
            }
        }
        string ans ; 
        for(int i  = 0 ; i < n ; i++){
            ans += finalState[i]  ;
        }
        return ans ; 
    }
};
/*
This solution is similar but it calculates the time taken by any 'L' or 'R' dominoes to reach at current index
and based on thid time we can calculate the final state
for more details see the solution  .
*/
class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size() ;
        vector<int>timeL(n , n+2) , timeR(n , n+2) ;
        int currTime = n+2 ;
        for(int i = 0 ; i < n ;i++){
            if(dominoes[i] == 'R'){
                currTime = 0 ;
            }
            else if(dominoes[i] == 'L'){
                currTime = n+2 ;
            }
            timeR[i] = currTime ;
            if(currTime < n+2){
                currTime++ ;
            }
        }
        currTime = n+2 ;
        for(int i = n-1; i >= 0 ; i--){
            if(dominoes[i] == 'L'){
                currTime = 0 ;
            }
            else if(dominoes[i] == 'R'){
                currTime = n+2 ;
            }
            timeL[i] = currTime ;
            if(currTime < n+2){
                currTime++ ;
            }
        }
        for(int i = 0 ; i < n ;i++){
            if(timeL[i] > timeR[i]){
                dominoes[i] = 'R' ;
            }
            else if(timeR[i] > timeL[i]){
                dominoes[i] = 'L' ;
            }
            else{
                dominoes[i] = '.' ;
            }
        }
        return dominoes ;
    }
};
