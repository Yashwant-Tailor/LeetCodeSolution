class Solution:
    def compress(self, chars: List[str]) -> int:
        # Solution Overview
        # use O(n*n) algorithm to update the values
        idx = 0
        t_len = 0
        while idx < len(chars):
            curr_char = chars[idx]
            t_len += 1
            idx += 1
            grp_len = 1
            grp_st_idx = idx
            while idx < len(chars) and chars[idx][0] == curr_char:
                grp_len += 1
                idx += 1
            if grp_len > 1:
                len_str = str(grp_len)
                len_idx = 0
                while len_idx < len(len_str):
                    chars[grp_st_idx] = len_str[len_idx]
                    len_idx += 1
                    grp_st_idx += 1
                    t_len += 1
                new_idx = grp_st_idx
                pop_char_cnt = idx - grp_st_idx
                while idx < len(chars):
                    chars[grp_st_idx],chars[idx] = chars[idx],chars[grp_st_idx]
                    grp_st_idx += 1
                    idx += 1
                idx = new_idx
                while pop_char_cnt > 0:
                    chars.pop()
                    pop_char_cnt -= 1
        return t_len

                
        
