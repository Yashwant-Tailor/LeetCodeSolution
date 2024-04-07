impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        use std::collections::HashSet ; 
        let mut open_ind = Vec::new();
        let mut delete_idx = HashSet::new();
        
        for (idx,c) in s.chars().enumerate() {
            match c {
                '(' => open_ind.push(idx),
                ')' => {
                    match open_ind.len() {
                        0 => {delete_idx.insert(idx);},
                        _ => {open_ind.pop();}
                    }
                },
                _ => ()
            }
        }
        for idx in open_ind.iter() {
            delete_idx.insert(*idx);
        }
        
        let mut new_str = String::new();
        for (idx , c) in s.chars().enumerate() {
            if !delete_idx.contains(&idx) {
                new_str.push(c);
            }
        }
        new_str
    }
}
