class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Solution Overview
        # take three pointer for count of each character ('a','b','c') let say ai,bi,ci
        # now set the pointer to location from the end such that suffix s[ai:] will have exactly k occurance of 'a' , same goes for bi and ci
        # now take a fourth pointer from the left side and maintain the count of each character and update the pointer ai ,bi and ci to overall have the count of each character equal to k , now take update the answer according to these four pointers

        right_idx_a = len(s)-1
        right_idx_b = len(s)-1
        right_idx_c = len(s)-1
        right_count_a = 0
        right_count_b = 0
        right_count_c = 0
        left_idx = 0
        while right_idx_a >= 0 and right_count_a < k:
            right_count_a += 1 if s[right_idx_a] == 'a' else 0
            right_idx_a -= 1
        right_idx_a += 1
        while right_idx_b >= 0 and right_count_b < k:
            right_count_b += 1 if s[right_idx_b] == 'b' else 0
            right_idx_b -= 1
        right_idx_b += 1
        while right_idx_c >= 0 and right_count_c < k:
            right_count_c += 1 if s[right_idx_c] == 'c' else 0
            right_idx_c -= 1
        right_idx_c += 1
        # if we don't have each type of character at least k times than return -1
        if right_count_a != k or right_count_b != k or right_count_c != k:
            return -1
        ans = len(s)-min([right_idx_a,right_idx_b,right_idx_c])
        while left_idx < len(s) and right_idx_a <= len(s) and right_idx_b <= len(s) and right_idx_c <= len(s):
            if s[left_idx] == 'a':
                if right_idx_a < len(s) and s[right_idx_a] == 'a':
                    right_idx_a += 1
                while right_idx_a < len(s) and s[right_idx_a] != 'a':
                    right_idx_a += 1
            if s[left_idx] == 'b':
                if right_idx_b < len(s) and s[right_idx_b] == 'b':
                    right_idx_b += 1
                while right_idx_b < len(s) and s[right_idx_b] != 'b':
                    right_idx_b += 1
            if s[left_idx] == 'c':
                if right_idx_c < len(s) and s[right_idx_c] == 'c':
                    right_idx_c += 1
                while right_idx_c < len(s) and s[right_idx_c] != 'c':
                    right_idx_c += 1
            curr_ans = left_idx + 1 + len(s) - min([right_idx_a,right_idx_b,right_idx_c])
            ans = min(ans,curr_ans)
            left_idx += 1
        return ans
