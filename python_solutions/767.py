class Solution:
    def reorganizeString(self, s: str) -> str:
        # Solution Oveview
        # if the maximum frequency of any character is greater than the half of the elements,then its not possible otherwise we can arrange the elements in some order to get any two adjacent character different
        # first make the frequency of maximum occuring character equal to second maximum orccuring character then place the character one by one
        char_cnt = [0 for i in range(26)]
        for char in s:
            char_idx = ord(char) - ord('a')
            char_cnt[char_idx] += 1
        arr = []
        for idx,cnt in enumerate(char_cnt):
            arr.append([cnt,idx])
        arr.sort(key = lambda x : x[0])
        if arr[-1][0] > (len(s)+1)//2:
            return ""
        final_str = ""
        if len(s)%2 == 1 and arr[-1][0] == (len(s)+1)//2:
            final_str += chr(arr[-1][1]+ord('a'))
            arr[-1][0] -= 1
        l_idx = 0
        while arr[-1][0] > arr[-2][0]:
            if arr[l_idx][0] == 0:
                l_idx += 1
            else:
                final_str += chr(arr[l_idx][1]+ord('a')) + chr(arr[-1][1] + ord('a'))
                arr[l_idx][0] -= 1
                arr[-1][0] -= 1
        while arr[-1][0] > 0:
            for idx in range(26):
                if arr[idx][0] > 0:
                    final_str += chr(arr[idx][1] + ord('a')) 
                    arr[idx][0] -= 1
        return final_str
        
