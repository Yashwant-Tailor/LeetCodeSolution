// recursion with little bit graph ( to store the map)
class Solution {
public:
    void FindAns(const vector<vector<char>>&adj ,int ind , const string & digits , vector<string>&ans ,string currMap ){
        if(ind  == digits.size()){
            ans.push_back(currMap) ;
            return ; 
        }
        int dig = digits[ind] -  '0' ; 
        for(int i = 0 ; i < adj[dig].size() ; i++){
            currMap.push_back(adj[dig][i]) ; 
            FindAns(adj , ind+1 , digits , ans , currMap) ; 
            currMap.pop_back() ;
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<vector<char>>adj(10) ; 
        adj[2].push_back('a');adj[2].push_back('b') ; adj[2].push_back('c') ;
        adj[3].push_back('d') ;adj[3].push_back('e') ;adj[3].push_back('f') ;
        adj[4].push_back('g') ; adj[4].push_back('h') ;adj[4].push_back('i') ; 
        adj[5].push_back('j') ;adj[5].push_back('k');adj[5].push_back('l');
        adj[6].push_back('m');adj[6].push_back('n') ;adj[6].push_back('o') ;
        adj[7].push_back('p');adj[7].push_back('q');adj[7].push_back('r');adj[7].push_back('s') ;
        adj[8].push_back('t') ;adj[8].push_back('u');adj[8].push_back('v');
        adj[9].push_back('w');adj[9].push_back('x');adj[9].push_back('y');adj[9].push_back('z') ;
        int ind =0 ; 
        vector<string>ans ; 
        if(digits.size() == 0){
            return ans ; 
        }
        string currMap = "" ; 
        FindAns(adj , ind , digits , ans , currMap) ;
        return ans ;
    }
};
