impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut nb = num_bottles ; 
        let mut ne = num_exchange ;
        let mut drunk : i32 = 0 ;
        while nb  > 0 {
            if nb >= ne {
                drunk += ne ; 
                nb -= ne ;
                nb += 1 ;
                ne += 1 ;   
            }
            else{
                drunk += nb ; 
                nb = 0 ;
            }
        }
        drunk
    }
}
