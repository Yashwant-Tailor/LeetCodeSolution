/*
simple implementation remember the logic for how roman numbers are formed from integer 
*/
class Solution {
public:
    string find_ans(int num){
        if(num == 0){
            return "" ; 
        }
        if(num == 1){
            return "I" ; 
        }
        else if(num == 5){
            return "V" ; 
        }
        else if(num == 10){
            return "X" ;
        }
        else if(num == 50){
            return "L"  ;
        }
        else if(num == 100){
            return "C" ; 
        }
        else if(num == 500){
            return "D" ; 
        }
        else if(num == 1000){
            return "M" ; 
        }
        if(num >= 1000){
            return "M" + find_ans(num - 1000) ; 
        }
        else if(num >= 900){
            return "CM" + find_ans(num - 900) ; 
        }
        else if(num >= 500){
            return "D" + find_ans(num -500) ; 
        }
        else if(num >= 400){
            return "CD" + find_ans(num - 400) ; 
        }
        else if(num >= 100){
            return "C" + find_ans(num - 100) ; 
        }
        else if(num >= 90){
            return "XC" + find_ans(num - 90) ; 
        }
        else if(num >= 50){
            return "L" + find_ans(num  - 50) ; 
        }
        else if(num >= 40){
            return "XL" + find_ans(num - 40) ; 
        }
        else if(num >= 10){
            return "X" + find_ans(num - 10) ; 
        }
        else if(num >= 9){
            return "IX" + find_ans(num - 9) ; 
        }
        else if(num >= 5){
            return "V" + find_ans(num - 5) ; 
        }
        else if(num >= 4){
            return "IV" + find_ans(num -4)  ;
        }
        else{
            return "I" + find_ans(num -1) ; 
        }
    }
    string intToRoman(int num) {
        return find_ans(num) ; 
    }
};
