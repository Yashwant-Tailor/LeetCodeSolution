impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        use std::cmp::{max,min} ;
        let (mut ls_min,mut ls_max,mut ls_out):(i64,i64,i64) = (0,0,0);
        let mut arr_cnt : i64 = 0 ;
        for (idx,value) in nums.iter().enumerate() {
            let new_idx = idx as i64 + 1 ;
            if *value == min_k {
                ls_min = new_idx; 
            }
            if *value == max_k {
                ls_max = new_idx ;
            }
            if *value < min_k || *value > max_k {
                ls_out = new_idx ;
            }
            arr_cnt += max(0 , min(ls_min,ls_max) - ls_out) ; 
        }
        arr_cnt
    }
}
