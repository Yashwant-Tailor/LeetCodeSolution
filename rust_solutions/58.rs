impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut prev_word_len:usize = 0;
        let mut itr = s.split(' ');
        while let Some(x) = itr.next() {
            let x_len = x.len() ;
            if x_len > 0 {
                prev_word_len = x_len ;
            }
        }
        prev_word_len as i32
    }
}
