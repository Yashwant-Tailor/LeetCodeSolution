// simple arithmetic implementation problem
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int add = 1 ; 
        int ind = digits.size() - 1; 
        while(ind >= 0){
            if(digits[ind]+add < 10){
                digits[ind] += add ; 
                return digits;
            }
            else{
                int temp = digits[ind] + add ; 
                digits[ind] = temp%10 ; 
                add = (temp - temp%10)/10 ; 
            }
            ind--;
        }
        if(add != 0){
            digits.insert(digits.begin() , add) ;
        }
        return digits ; 
    }
};
