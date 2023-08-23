class Solution:
    def reorganizeString(self, s: str) -> str:
        # Solution Oveview
        # if the maximum frequency of any character is greater than the half of the elements,then its not possible otherwise we can arrange the elements in some order to get any two adjacent character different
        # first make the frequency of maximum occuring character equal to second maximum orccuring character then place the character one by one
        char_cnt = [0 for i in range(26)]
        for char in s:
            char_idx = ord(char) - ord('a')
            char_cnt[char_idx] += 1
        import heapq as hp
        cnt_max_heap = []
        for idx,cnt in enumerate(char_cnt):
            hp.heappush(cnt_max_heap,[-cnt,idx])
        curr_elm = hp.heappop(cnt_max_heap)
        if -curr_elm[0] > (len(s)+1)//2:
            return ""
        final_str = ""
        while curr_elm[0] < 0:
            char = chr(curr_elm[1] + ord('a'))
            final_str += char
            next_elm = hp.heappop(cnt_max_heap)
            curr_elm[0] += 1 # as we have put negative frequency in our heap , to maintain the maximum heap property (not minimum heap)
            hp.heappush(cnt_max_heap,curr_elm)
            curr_elm = next_elm
        return final_str
        
