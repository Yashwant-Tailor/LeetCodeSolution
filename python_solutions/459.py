class Solution:
    def get_factors(self,num):
        fac = []
        curr_fac = 1
        while curr_fac * curr_fac <= num:
            if num%curr_fac == 0:
                fac.append(curr_fac)
            if curr_fac != num//curr_fac:
                fac.append(num//curr_fac)
            curr_fac += 1
        return fac
    def get_gcd(self,char_cnt):
        from math import gcd
        t_gcd = 0
        for cnt in char_cnt:
            t_gcd = gcd(t_gcd,cnt)
        return t_gcd
    def is_pos(self,fac,char_cnt,s):
        sub_str_char_cnt = [cnt//fac for cnt in char_cnt]
        total_char_cnt = sum(sub_str_char_cnt)
        sub_str_len = total_char_cnt
        max_idx = 0
        for char in s:
            char_idx = ord(char) - ord('a')
            if sub_str_char_cnt[char_idx] > 0:
                total_char_cnt -= 1
                sub_str_char_cnt[char_idx] -= 1
            elif total_char_cnt > 0:
                return False
            if total_char_cnt == 0:
                break
        if len(s) == sub_str_len or len(s)%sub_str_len != 0:
            return False
        left_end = 0
        right_end = sub_str_len
        sub_str = s[left_end : right_end]
        while right_end <= len(s):
            curr_sub_str = s[left_end:right_end]
            if sub_str != curr_sub_str:
                return False
            left_end = right_end
            right_end += sub_str_len
        return True

    def repeatedSubstringPattern(self, s: str) -> bool:
        # Solution Overview
        # the occurance of every character should be some multiple (i.e. it will copies of that substring)
        # after that we will find the gcd of the count of character in the string
        # then for each factor of our gcd we will try to find that a substring , having total_count/factor many character (same) will is repeated substring or not
        
        char_cnt = [0 for i in range(26)]
        for char in s:
            char_idx = ord(char)-ord('a')
            char_cnt[char_idx] += 1
        gcd = self.get_gcd(char_cnt)
        factors = self.get_factors(gcd)
        for fac in factors:
            can_make_sub_str = self.is_pos(fac,char_cnt,s)
            if can_make_sub_str:
                return True
        return False
        
