impl Solution {
    pub fn count_alternating_subarrays(nums: Vec<i32>) -> i64 {
        let mut arr_cnt:i64 = 0 ;
        let mut idx : usize = 0 ; 
        let nums_len = nums.len() ; 
        while idx < nums_len {
            let mut arr_len :i64 = 1 ; 
            let mut curr_num = nums[idx] ;
            idx += 1 ;
            while idx < nums_len && nums[idx] != curr_num {
                curr_num = nums[idx] ; 
                idx += 1 ; 
                arr_len += 1 ;
            }
            arr_cnt += (arr_len * (arr_len + 1))/2 ;
        }
        arr_cnt
    }
}
