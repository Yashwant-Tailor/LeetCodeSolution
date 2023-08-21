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
    def is_pos(self,sub_str_len,s):
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
        factors = self.get_factors(len(s))
        for fac in factors:
            can_make_sub_str = self.is_pos(fac,s)
            if can_make_sub_str:
                return True
        return False
        
