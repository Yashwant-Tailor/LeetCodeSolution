impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        use std::collections::HashMap ; 
        let mut s2t : HashMap<char,char> = HashMap::new();
        let mut t2s : HashMap<char,char> = HashMap::new();
        let mut sitr = s.chars() ;
        let mut titr = t.chars() ;
        while let (Some(s_char),Some(t_char)) = (sitr.next(),titr.next()){
            match (s2t.get(&s_char),t2s.get(&t_char)){
                (Some(&st_char),Some(&ts_char)) => {
                    if st_char != t_char || ts_char != s_char {
                        return false
                    }
                },
                (None,None) => {
                    s2t.insert(s_char,t_char);
                    t2s.insert(t_char,s_char);
                },
                _ => return false
            }
        }
        true
    }
}
