/*
Simple DP probelem 
points to rememeber
1. convert the expression in array where we will have the integer and the operator ( see convert_int function more detail )
2. after testing on one test case I got to know that leading '+' or  '-' is not allowed (ex. "+1-2").
So you can say that for every operator will act like binary operator.
3. after observing the above point writing the recursive function is not very hard ,
for every range (l to r ) we will traverse the range find one operator and then we will evalute the left and right side and combine the result based on current operator .
This will be answer for the range(l to r)
4. base case will be when l == r i.e. we don't have any operator its just number .
*/
class Solution {
public:
    vector<int> cal_ans(const vector<int>&expression , int l , int r){
        if(l == r){
            vector<int>base_case ; 
            base_case.push_back(expression[l]) ; 
            return base_case ; 
        }
        vector<int>ans ; 
        for(int i = l+1 ; i < r ; i += 2){
            vector<int> ansL = cal_ans(expression , l , i-1) ; 
            vector<int> ansR = cal_ans(expression , i+1 , r) ; 
            
            for(int j = 0 ; j < (int)ansL.size() ; j++){
                for(int k = 0 ; k < (int)ansR.size() ; k++){
                    if(expression[i]==0){
                        ans.push_back(ansL[j] + ansR[k]) ; 
                    }
                    else if(expression[i] ==1){
                        ans.push_back(ansL[j]  - ansR[k]) ;
                    }
                    else{
                        ans.push_back(ansL[j] * ansR[k]) ; 
                    }
                }
            }
        }
        return ans ; 
    }
    vector<int> convert_int(string expression){
        int st = 0 , en = (int)expression.size() ; 
        vector<int>ans ; 
        while(st < en){
            int num = 0;
            while(st < en && expression[st] - '0' >= 0 && expression[st]-'0' <= 9){
                num *= 10 ; 
                num += expression[st] - '0'  ;
                st++ ; 
            }
            ans.push_back(num) ; 
            
            if(st != en){
                if(expression[st] == '+' ){
                    ans.push_back(0) ; 
                }
                else if(expression[st] == '-'){
                    ans.push_back(1) ; 
                }
                else{
                    ans.push_back(2) ; 
                }
                st++  ;
            }
        }
        
        return ans ; 
    }
    vector<int> diffWaysToCompute(string expression) {
        vector<int>exp = convert_int(expression)  ; 
        int n = (int)exp.size() ;
        return cal_ans(exp , 0 , n -1  ) ;
    }
};
