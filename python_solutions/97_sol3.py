class Solution:
    def isPos(self,s1,s2,s3,sub_s1_len,sub_s2_len,sub_s3_len,is_intrlv):
        s1_idx = sub_s1_len
        s2_idx = sub_s2_len
        s3_idx = sub_s3_len
        cnt = 0
        while s1_idx > 0 and s1[s1_idx-1] == s3[s3_idx-1]:
            cnt += 1
            if is_intrlv[(sub_s3_len-cnt,sub_s1_len-cnt)]:
                return True
            s1_idx -= 1
            s3_idx -= 1
        cnt = 0
        s3_idx = sub_s3_len
        while s2_idx > 0 and s2[s2_idx-1] == s3[s3_idx-1]:
            cnt += 1
            if is_intrlv[(sub_s3_len-cnt,sub_s1_len)]:
                return True
            s2_idx -= 1
            s3_idx -= 1
        return False
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Solution Overview
        # dp[i] = will store that if it is possible to get the s3[0:i] , by interleaving all the substring of s1 of length n and s2 of length m , where n + m == i 

        s3_len = len(s3)
        s2_len = len(s2)
        s1_len = len(s1)
        if s1_len + s2_len != s3_len :
            return False
        from collections import defaultdict
        is_intrlv = defaultdict(lambda : False)
        is_intrlv[(0,0)] = True
        for sub_s3_len in range(1,s3_len+1):
            sub_s2_len = min(s2_len,sub_s3_len)
            sub_s1_len = sub_s3_len - sub_s2_len
            while sub_s2_len >= 0 and sub_s1_len <= s1_len:
                is_intrlv[(sub_s3_len,sub_s1_len)] |= self.isPos(s1,s2,s3,sub_s1_len,sub_s2_len,sub_s3_len,is_intrlv)
                sub_s2_len -= 1
                sub_s1_len += 1
        return is_intrlv[(s3_len,s1_len)]
