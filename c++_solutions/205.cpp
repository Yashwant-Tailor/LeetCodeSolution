class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char,char> s2t , t2s ; 
        auto sitr = s.begin() ;
        auto titr = t.begin() ; 
        while (sitr != s.end() && titr != t.end()){
            auto st_char = s2t.find(*sitr);
            auto ts_char = t2s.find(*titr);
            if (st_char != s2t.end() && ts_char != t2s.end()){
                if ((st_char->second != *titr) || (ts_char->second != *sitr)){
                    return false;
                }
            }
            else if (st_char == s2t.end() && ts_char == t2s.end()){
                s2t[*sitr] = *titr ;
                t2s[*titr] = *sitr ;
            }
            else{
                return false;
            }
            sitr++;
            titr++;
        }
        return true ;
    }
};
