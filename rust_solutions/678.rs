impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut open = Vec::new();
        let mut star = Vec::new();
        for (idx,c) in s.chars().enumerate() {
            match c {
                '(' => {open.push(idx);},
                '*' => {star.push(idx);},
                _ => {
                    if open.len() > 0{
                        open.pop();
                    }
                    else if star.len() > 0 {
                        star.pop();
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        
        while open.len() > 0 {
            if star.len() == 0 {
                return false;
            }
            match (open.pop() , star.pop()) {
                (Some(x),Some(y)) => {if x > y {return false;}},
                (Some(x),None) => {return false;},
                _ => {break ;}
            }
        }
        
        true
    }
}
