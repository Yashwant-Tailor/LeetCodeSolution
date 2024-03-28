impl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut right:usize = 0;
        let mut prod : i32 = 1 ;
        let mut total_cnt : i32 = 0 ; 
        for left in 0..nums.len() {
            if right < left {
                right = left  ;
                prod = 1 ;
            }
            while right < nums.len() && prod * nums[right] < k {
                prod *= nums[right] ;
                right += 1;
            }
            total_cnt += (right - left) as i32;
            prod /= nums[left] ;
        }
        total_cnt
    }
}
