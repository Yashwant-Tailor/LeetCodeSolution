/*
let's say we know solution for the string s[1:i-1] and now we want to calculate the answer for string s[1:i]
there are two possible transition for this state , 
Transition 1 : s[i] is valid mapping i.e. s[i] != '0' 
if this is the case then DP[i] = DP[i] + DP[i-1] 
Transition 2: s[i-1:i] is valid mapping (see the isValidMapping function for detail)
if this is the case then DP[i] = DP[i] + DP[i-2]
*/
class Solution {
public:
    bool isValidMapping(string s){
        if(s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9"){
            return true ;
        }
        if(s == "10" or s == "11" or s == "12" or s == "13" or s == "14" or s == "15" or s == "16" or s == "17" or s == "18" or s == "19"){
            return true ;
        }
        if(s == "20" or s == "21" or s == "22" or s == "23" or s == "24" or s == "25" or s == "26"){
            return true ; 
        }
        return false ;
    }
    int numDecodings(string s) {
        int n = s.size() ; 
        vector<int>DP(n+1 , 0) ; 
        DP[0] = 1; 
        for(int  i = 1; i <= n ; i++){
            string check = "" ;
            check += s[i-1] ;
            if(check != "0"){
                DP[i] += DP[i-1] ; 
            }
            if(i != 1){
                check = s[i-2] + check ; 
            }
            
            if(i != 1 && isValidMapping(check)){
                DP[i] += DP[i-2] ; 
            }
        }
        
        return DP[n] ; 
    }
};
