impl Solution {
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        let mut prev_deck = deck.clone() ; 
        use std::collections::LinkedList ; 
        let mut ind = LinkedList::new() ; 
        for idx in 0..deck.len() {
            ind.push_back(idx);
        }
        prev_deck.sort_unstable() ; 
        let mut new_deck = vec![0;deck.len()] ;
        for num in prev_deck.iter() {
            let idx = match ind.pop_front() {
                Some(idx) => idx ,
                _ => 0
            };
            new_deck[idx] = *num ; 
            if let Some(idx) = ind.pop_front() {
                ind.push_back(idx) ;
            }
        }
        
        new_deck
    }
}
