class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.begin() , deck.end());
        vector<int> new_deck(deck.size());
        queue<int>ind ; 
        for(size_t idx = 0 ; idx < deck.size() ; idx++){
            ind.push(idx) ;
        }
        size_t idx = 0 ;
        while(idx < deck.size()){
            new_deck[ind.front()] = deck[idx] ; 
            idx++;
            ind.pop();
            if(ind.size() != 0){
                auto elm = ind.front();
                ind.pop();
                ind.push(elm);
            }
        }
        return new_deck ; 
    }
};
