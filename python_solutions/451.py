class Solution:
    def frequencySort(self, s: str) -> str:
        # Solution Overview
        # maintain frequency and then sort the string
        from collections import defaultdict
        cnt = defaultdict(lambda : 0)
        for char in s:
            cnt[char] += 1
        cnt_arr = []
        for char,char_cnt in cnt.items():
            cnt_arr.append((char,char_cnt))
        cnt_arr.sort(key=lambda x : x[1],reverse=True)
        sort_str = ""
        idx = 0 
        while idx < len(cnt_arr):
            char , char_cnt = cnt_arr[idx]
            while char_cnt > 0:
                char_cnt -= 1
                sort_str += char
            idx += 1
        return sort_str
        
