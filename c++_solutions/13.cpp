/*
rememeber the logic how to form a roman number from integer 
implementation simple
*/
class Solution {
public:
    int find_ans(string & s , int ind){
        if(ind < 0){
            return 0 ; 
        }
        if(ind == 0){
            if(s[ind] == 'M'){
                return 1000 ; 
            }
            else if(s[ind] == 'D'){
                return 500 ; 
            }
            else if(s[ind] == 'C'){
                return 100 ; 
            }
            else if(s[ind] == 'L'){
                return 50 ; 
            }
            else if(s[ind] == 'X'){
                return 10 ; 
            }
            else if(s[ind ]== 'V'){
                return 5 ; 
            }
            else{
                return 1 ; 
            }
        }
        if(s[ind] == 'M' && s[ind-1] == 'C'){
            return find_ans(s , ind-2) + 900 ; 
        }
        if(s[ind] == 'D' && s[ind-1] == 'C'){
            return find_ans(s , ind-2) + 400 ; 
        }
        if(s[ind] == 'C' && s[ind-1] == 'X'){
            return find_ans(s,  ind-2) + 90 ; 
        }
        if(s[ind] == 'L' && s[ind-1] == 'X'){
            return find_ans(s , ind-2) + 40  ;
        }
        if(s[ind] == 'X' && s[ind-1] == 'I'){
            return find_ans(s , ind-2) + 9 ; 
        }
        if(s[ind ]=='V' && s[ind-1] == 'I'){
            return find_ans(s , ind-2) + 4 ; 
        }
        if(s[ind] == 'M'){
            return 1000 + find_ans(s , ind-1) ; 
        }
        if(s[ind] == 'D'){
            return 500 + find_ans(s , ind-1) ; 
        }
        if(s[ind] == 'L'){
            return 50 + find_ans(s , ind-1) ; 
        }
        if(s[ind ]== 'C'){
            return 100 + find_ans(s , ind-1) ; 
        }
        if(s[ind] == 'X'){
            return 10 + find_ans(s , ind-1) ; 
        }
        if(s[ind] == 'V'){
            return 5 + find_ans(s , ind-1) ; 
        }
        return 1 + find_ans(s , ind-1) ; 
    }
    int romanToInt(string s) {
        return find_ans(s , s.size()-1) ; 
    }
};
