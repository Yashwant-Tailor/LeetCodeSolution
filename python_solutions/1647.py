class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = [0 for i in range(26)]
        for char in s:
            cnt[ord(char)-ord('a')] += 1
        cnt.sort()
        idx = len(cnt)-1
        del_cnt = 0
        val = int(1e6)
        while idx >= 0:
            if val > cnt[idx]:
                val = cnt[idx]
            eq_num = cnt[idx]
            while idx >= 0 and eq_num == cnt[idx]:
                del_cnt += abs(val-cnt[idx])
                idx -= 1
                if val > 0:
                    val -= 1
        return del_cnt
            
        
