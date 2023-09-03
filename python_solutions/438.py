class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Solution Overview
        # we can maintain the count of character in p , then use two pointers to keep track of anagram's in s
        from collections import defaultdict
        freq_p = defaultdict(lambda :0)
        for char in p:
            freq_p[char] += 1
        left_idx = 0
        right_idx = 0
        curr_freq = defaultdict(lambda  : 0)
        req_char = len(p)
        ana_idx = []
        while right_idx < len(s):
            if s[right_idx] not in freq_p:
                curr_freq.clear()
                right_idx += 1
                req_char = len(p)
                left_idx = right_idx
            else:
                curr_freq[s[right_idx]] += 1
                if s[right_idx] in freq_p:
                    req_char -= 1
                while curr_freq[s[right_idx]] > freq_p[s[right_idx]]:
                    curr_freq[s[left_idx]] -= 1
                    req_char += 1
                    left_idx += 1
                if req_char == 0:
                    ana_idx.append(left_idx)
                right_idx += 1
        return ana_idx
        
