class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Solution Overview
        # we can solve the problem using two pointers
        # lets maintain two pointers left and right in s, 
        # and find first substring which contains all the character in t
        # update the left and right accordingly to get next substring


        from collections import defaultdict
        freq_t = defaultdict(lambda : 0)
        for char in t:
            freq_t[char] += 1
        req_char_cnt = len(t)
        left = 0
        right = 0
        ans_left = -1
        ans_right = -1
        while right < len(s):
            left_char = s[left]
            right_char = s[right]
            if req_char_cnt > 0:
                if right_char in freq_t:
                    if freq_t[right_char] > 0:
                        req_char_cnt -= 1
                    freq_t[right_char] -= 1
                right += 1
            else:
                if ans_right == -1  or  (ans_right-ans_left+1) > (right-left):
                    ans_right = right-1
                    ans_left = left
                if left_char in freq_t:
                    freq_t[left_char] += 1
                    if freq_t[left_char] == 1:
                        req_char_cnt +=1
                left += 1
        while req_char_cnt == 0 and left < len(s):
            left_char = s[left]
            if ans_right == -1  or  (ans_right-ans_left+1) > (right-left):
                ans_right = right-1
                ans_left = left
            if left_char in freq_t:
                freq_t[left_char] += 1
                if freq_t[left_char] == 1:
                    req_char_cnt +=1
            left += 1
        return "" if ans_right == -1 else s[ans_left:ans_right+1]
