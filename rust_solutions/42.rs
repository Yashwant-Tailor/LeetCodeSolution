impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        use std::cmp::{max,min} ; 
        let mut LH_MAX = Vec::new() ; 
        let mut seen_max_height : i32 = -1 ; 
        for h in height.iter() {
            seen_max_height = max(seen_max_height , *h) ; 
            LH_MAX.push(seen_max_height) ; 
        }
        seen_max_height = -1 ; 
        let mut water_trapped : i32 = 0 ;
        for (idx,h) in height.iter().enumerate().rev() {
            seen_max_height = max(seen_max_height , *h) ; 
            water_trapped += (*h - min(LH_MAX[idx],seen_max_height)).abs() ;
        }
        water_trapped
    }
}
