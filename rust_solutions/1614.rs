impl Solution {
    pub fn max_depth(s: String) -> i32 {
        use std::cmp::max;
        let mut curr_depth:i32 = 0 ;
        let mut max_depth: i32 = 0 ;
        for c in s.chars() {
            match c {
                '(' => curr_depth += 1 ,
                ')' => curr_depth -= 1 ,
                _ => () ,
            }
            max_depth = max(max_depth , curr_depth) ;
        }
        max_depth
    }
}
