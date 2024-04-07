class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int cnt_par = 0 ; 
        size_t idx = 0 ;
        stack<size_t>open_ind ; 
        unordered_set<size_t> delete_idx ; 
        while(idx < s.size()){
            if(s[idx] == '('){
                open_ind.push(idx);
            }
            else if(s[idx] == ')'){
                if(open_ind.size() > 0){
                    open_ind.pop();
                }
                else{
                    delete_idx.insert(idx);
                }
            }
            idx++ ;
        }
        while(open_ind.size() > 0){
            delete_idx.insert(open_ind.top());
            open_ind.pop();
        }
        string new_str = "";
        for(idx = 0 ; idx < s.size() ; ++idx){
            if(delete_idx.find(idx) == delete_idx.end()){
                new_str += s[idx] ;
            }
        }
        return new_str ;
    }
};
