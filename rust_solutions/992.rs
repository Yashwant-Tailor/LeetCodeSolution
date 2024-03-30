impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap ;
        let mut freq : HashMap<i32,i32> = HashMap::new() ; 
        let (mut l,mut r1,mut r2):(usize , usize,usize) = (0,0,0);
        let nums_len = nums.len(); 
        let mut arr_cnt:usize = 0;
        let mut k1  = k as usize ;
        while l < nums_len {
            while r1 < nums_len && freq.len() < k1 {
                if let Some(x) = freq.get_mut(&nums[r1]) {
                    *x += 1 ;
                }
                else{
                    freq.insert(nums[r1],1);
                }
                if r1 == r2 {
                    r2 += 1 ;
                }
                r1 += 1 ;
            }
            while r2 < nums_len {
                if let Some(x) = freq.get(&nums[r2]) {
                    r2 += 1;
                }
                else{
                    break ;
                }
            }
            if freq.len() == k1 {
                arr_cnt += r2-r1 + 1;
            }
            if let Some(x) = freq.get_mut(&nums[l]){
                *x -= 1 ;
                if *x == 0 {
                    freq.remove(&nums[l]);
                }
            }
            l += 1 ;
        }
        arr_cnt as i32
    }
}
