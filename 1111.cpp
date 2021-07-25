/*
maintain an connt of openigparantheses
and also a variable which tells us where we need to put the current opening parantheses
if current character is opening parantheses then we will add it to the based on the adding variable information
if current character is closed parantheses then we will in reverse of the adding varaible information 
see the solution of more information .
*/
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.size() ; 
        bool addA = true ; 
        vector<int>ans(n , -1) ; 
        int countOpening = 0 ; 
        for(int i = 0 ; i< n ;i++){
            if(seq[i] == '('){
                countOpening++ ;
                if(addA){
                    ans[i] = 0 ; 
                    addA = false ; 
                }
                else{
                    ans[i] = 1  ;
                    addA = true ; 
                }
            }
            else{
                countOpening--;
                if(!addA){
                    ans[i] = 0  ;
                }
                else{
                    ans[i] = 1 ; 
                }
                addA = addA ? false : true  ; 
            }
        }
        return ans ; 
    }
};
