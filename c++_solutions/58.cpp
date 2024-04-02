class Solution {
public:
    int lengthOfLastWord(string s) {
        size_t prev_word_len = 0;
        for (auto it = s.begin() ; it != s.end() ;){
            while (it != s.end() && *it == ' '){
                it++;
            }
            if (it != s.end()){
                prev_word_len = 0;
                while(it != s.end() && *it != ' '){
                    prev_word_len++;
                    it++;
                }
            }
        }
        return prev_word_len ;
        
    }
};
