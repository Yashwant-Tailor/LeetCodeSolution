/*
W.L.O.G. we assume that a < b ( otherwise we swap the value of a and b and also the character) .
if 2*a + 2 < b :
    then the answer is not possible 
else 
    first we wil see if 2*a < b then we subtract will set b = 2 * a and store the extra value in b in some other variable and in the last we will add this character
     then we will place the "bb" with "a" and decrease the count of a by 1 and b by 2
    at some some place during the above operation we will have that a == b
    so now we will place "b" with "a" and decrease a by 1 till a not become zero
    now we will place the extra character b we had in the starting 
*/
class Solution {
public:
    string strWithout3a3b(int a, int b) {
        char c1 = 'a' , c2 = 'b' ; 
        if(a > b){
            swap(a , b)  ;
            swap(c1 , c2) ; 
        }
        string ans ; 
        int add= 0 ; 
        if(2*a < b){
            add += b - 2*a ; 
            b = 2*a ; 
        }
        while( a != b){
            ans += c2 ; ans += c2 ; 
            ans += c1 ; 
            a-- ; b--;b--;
        }
        while(a--){
            ans += c2 ; ans += c1 ;
        }
        while(add--){
            ans += c2 ; 
        }
        return ans ; 
    }
};
