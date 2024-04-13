impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        use std::cmp::max ;
        let mut bar_height = vec![vec![0;matrix[0].len()];matrix.len()] ;
        for col in 0..matrix[0].len() {
            for row in (0..matrix.len()).rev() {
                if row + 1 < matrix.len() {
                    bar_height[row][col] += bar_height[row+1][col] ;
                }
                match matrix[row][col] {
                    '1' => {bar_height[row][col] += 1;} ,
                    '0' => {bar_height[row][col] = 0;} ,
                    _ => () 
                };
            }
        }
        
        let mut bar_stack = Vec::<usize>::new() ;
        let mut L = vec![0 as usize ; matrix[0].len()];
        let mut rec_area = 0 ;
        for row in 0..matrix.len() {
            bar_stack.clear() ; 
            for col in 1..(matrix[0].len()+1) {
                while let Some(&idx) = bar_stack.last() {
                    if bar_height[row][idx-1] >= bar_height[row][col-1] {
                        bar_stack.pop();
                    }
                    else{
                        break;
                    }
                }
                L[col-1] = match bar_stack.len() {
                    0 => 0 ,
                    _ => *bar_stack.last().unwrap()
                };
                bar_stack.push(col) ;
            }
            bar_stack.clear() ;
            
            for col in (1..(matrix[0].len()+1)).rev() {
                while let Some(&idx) = bar_stack.last() {
                    if bar_height[row][idx-1] >= bar_height[row][col-1] {
                        bar_stack.pop() ;
                    }
                    else{
                        break ;
                    }
                }
                let Ri = match bar_stack.len() {
                    0 => matrix[0].len()+1 , 
                    _ => *bar_stack.last().unwrap()
                };
                bar_stack.push(col);
                rec_area = max(rec_area , ((Ri - L[col-1] -1 ) * bar_height[row][col-1]) as i32);
            }
        }
        
        rec_area 
    }
}
