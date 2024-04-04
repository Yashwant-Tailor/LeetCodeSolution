class Solution {
public:
    int maxDepth(string s) {
        int curr_depth = 0 , max_depth = 0 ; 
        for (char const & c  : s){
            switch(c){
                case '(':
                    curr_depth++;
                    break ;
                case ')':
                    curr_depth--;
                    break;
            }
            max_depth = max(max_depth , curr_depth);
        }
        return max_depth ;
    }
};
