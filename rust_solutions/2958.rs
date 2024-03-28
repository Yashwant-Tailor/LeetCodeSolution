impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap ;
        use std::cmp::max;
        let mut freq : HashMap<i32,i32> = HashMap::new();
        let (mut left,mut max_len) : (usize,usize) = (0,0);
        for (idx,value) in nums.iter().enumerate() {
            while let curr_elm_cnt = freq.entry(*value).or_insert(0) {
                if *curr_elm_cnt < k {
                    break ;
                }
                let curr_left_elm_cnt = freq.entry(nums[left]).or_insert(0);
                *curr_left_elm_cnt -= 1 ;
                left += 1;
            }
            max_len = max(max_len , idx - left + 1);
            freq.entry(*value).and_modify(|elm| {*elm += 1 });
        }
        max_len as i32
    }
}
