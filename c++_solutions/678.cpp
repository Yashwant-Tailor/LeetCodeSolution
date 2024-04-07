class Solution {
public:
    bool checkValidString(string s) {
        stack<size_t> open , star ;
        for(size_t idx = 0 ; idx < s.size(); ++idx){
            if( s[idx] == '('){
                open.push(idx);
            }
            else if(s[idx] == '*'){
                star.push(idx);
            }
            else{
                if (open.size() > 0){
                    open.pop() ;
                }
                else if(star.size() > 0){
                    star.pop();
                }
                else{
                    return false;
                }
            }
        }
        
        while(open.size() > 0){
            if (star.size() == 0){
                return false;
            }
            else if (open.top() < star.top()){
                open.pop(); star.pop();
            }
            else{
                return false;
            }
        }
        return true;
    }
};
