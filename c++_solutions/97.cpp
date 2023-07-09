/*
Great problem for somebody who just started with DP or not able to use DP in advanced problem.
I have seen problems in which I have to use DP technique but those are just classic problem , 
i.e. somebody can solve those problem using simple exponentiation or bottom up approach . 
This problem also used the concept of bottom up but in somewhat different way .
So if you're begginer then I really recommend you to understand every bit (how to solve) of this problem .
!!!!Happy Coding!!!!
*/
/*
Hint 1: try to calculate the answer for length i of s3
Hint 2: if we calculate the answer for s3 of length i and in the answer the length used from s1 is j and length used from s3 is k then it must hold that (j + k = i)
Hint 3: if we calculate the answer for s3[1:i] then for i1 in {1,2,3...i-1} , s3[i1:i] should belong to either s1 or s2
Hint 4: think about the transition we can have using the above hints
*/
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.size() , m = s2.size() , nm = s3.size() ; 
        if(n + m != nm){
            return false ;
        }
        vector<vector<vector<bool>>>DP(n+1, vector<vector<bool>>(m+1 , vector<bool>(2 , false))) ; 
        DP[0][0][0] = true , DP[0][0][1] = true ; 
        for(int i = 1 ; i <= nm ; i++){
            for(int j  = i ; j >= 0 ; j--){
                int k = i - j ; 
                if(j <= n && k <= m){
                    bool isS = true , isT = true ;
                    int temp_i = i - 1; 
                    while(temp_i >= 0 && (isS || isT)){
                        if(isS && j - (i - temp_i) >= 0  && s3[temp_i] == s1[j - (i - temp_i)]){
                            if(DP[j - (i - temp_i)][k][1]){
                                DP[j][k][0] = true; 
                            }
                        }
                        else{
                            isS = false ;
                        }
                        if(isT && k - (i - temp_i) >= 0 && s3[temp_i] == s2[k - (i - temp_i)]){
                            if(DP[j][k - (i - temp_i)][0]){
                                DP[j][k][1]  = true ;
                            }
                        }
                        else{
                            isT = false ; 
                        }
                        temp_i--;
                    }
                }
            }
        }
        bool ans = false ; 
        for(int j = 0 ; j <= nm ; j++){
            if(j <= n && nm - j <= m){
                ans |= (DP[j][nm-j][0] || DP[j][nm-j][1]) ; 
            }
        }
        return ans ; 
    }
};
