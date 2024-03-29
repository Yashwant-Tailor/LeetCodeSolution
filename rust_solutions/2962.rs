impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let nums_size = nums.len();
        let max_val = *nums.iter().max().unwrap() ;
        let mut arr_cnt : i64 = 0 ;
        let mut max_loc:Vec<usize> = Vec::new();
        max_loc.push(0);
        for (idx,value) in nums.iter().enumerate() {
            if *value == max_val {
                max_loc.push(idx+1);
            }
        }
        max_loc.push(nums_size+1);
        let add_idx : usize = k as usize - 1;
        for idx in 1..nums_size+1 {
            match max_loc.get(idx + add_idx) {
                Some(&next_loc) => {
                    arr_cnt += (max_loc[idx]-max_loc[idx-1]) as i64 * (nums_size-next_loc+1) as i64 ;
                },
                None => break
            }
        }
        arr_cnt
        
    }
}
