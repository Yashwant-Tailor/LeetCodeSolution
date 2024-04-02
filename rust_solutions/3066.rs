impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        use std::collections::BinaryHeap ;
        use std::cmp::{min,max} ;
        let mut min_heap:BinaryHeap<i64> = BinaryHeap::new() ;
        for num in nums.iter() {
            min_heap.push( (*num * -1)as i64 );
        }
        let mut op_cnt:i32 = 0 ;
        while let (Some(x),Some(y)) = (min_heap.pop(),min_heap.pop()) {
            let (mi,ma) = (min(-1*x,-1*y),max(-1*x,-1*y));
            if mi < k as i64 {
                op_cnt += 1 ;
                min_heap.push((mi*2+ma)* -1) ;
            }
            else{
                break;
            }
        }
        op_cnt
        
    }
}
