class Solution:
    def get_string_with_rep_char(self, idx, s):
        ans_len = 0
        if idx < len(s):
            compare_char = s[idx]
            while idx < len(s) and compare_char == s[idx]:
                ans_len += 1
                idx += 1
        return idx, ans_len

    def get_string_without_rep_char(self, idx, s):
        ans_len = 0
        if idx < len(s):
            compare_char = None
            while idx < len(s) :
                if compare_char is None:
                    compare_char = s[idx]
                elif compare_char == s[idx]:
                    break
                else:
                    compare_char = s[idx]
                ans_len += 1
                idx += 1
            # as we have counted one repeated character just remove it from the count the set the idx correctly
            if idx < len(s):
                idx -= 1
                ans_len -= 1
        return idx, ans_len

    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        # Solution Overview
        # if we have a pair of consecutive digits with length equal to 2 then semi-repitive string which will include this pair would be of length 2 + 1(last character of pair left to it) + length of string in between left and this pair + 1(starting character of the pair right to it ) + length of string in between this and right pair
        # if we have a pair of consecutive digits with length greater than 2 then semi-repitive string which will include this pair would be string which will have greater length in following two cases
        # CASE1 :
        # 2 (character on the left end of consecutive digits string) + length of string in between left and this pair + 1(last character of the pair left to it)
        # CASE2:
        # 2 (character on the right end of the consecutive digits string) + length of string in between this and right pair + 1(first character of the pair right to it)

        idx = 0
        prev_consecutive_length = 0
        next_consecutive_length = 0
        curr_consecutive_length = 0
        left_string_length = 0
        right_string_length = 0
        ans = 0
        while idx < len(s):
            prev_consecutive_length = curr_consecutive_length
            curr_consecutive_length = next_consecutive_length
            left_string_length = right_string_length
            idx, right_string_length = self.get_string_without_rep_char(idx, s)
            idx, next_consecutive_length = self.get_string_with_rep_char(idx, s)
            curr_semi_repitive_length = 0
            if curr_consecutive_length == 0:
                curr_semi_repitive_length = right_string_length
            elif curr_consecutive_length == 2:
                curr_semi_repitive_length = curr_consecutive_length + left_string_length + right_string_length
                # if we have left previous consecutive character then we can take one character from this string
                if prev_consecutive_length > 0:
                    curr_semi_repitive_length += 1
                # if we have left next consecutive character then we can take one character from this string
                if next_consecutive_length > 0:
                    curr_semi_repitive_length += 1
            else:
                curr_semi_repitive_length_left = 2 + left_string_length
                # if we have left previous consecutive character then we can take one character from this string
                if prev_consecutive_length > 0:
                    curr_semi_repitive_length_left += 1
                curr_semi_repitive_length_right = 2 + right_string_length
                # if we have left next consecutive character then we can take one character from this string
                if next_consecutive_length > 0:
                    curr_semi_repitive_length_right += 1
                curr_semi_repitive_length = max(curr_semi_repitive_length_left,curr_semi_repitive_length_right)
            ans = max(ans,curr_semi_repitive_length)
        # final calculate the answer for the last consecutive pair
        if next_consecutive_length == 0:
            ans = max(ans,right_string_length)
        elif next_consecutive_length >= 2:
            ans = max(ans,2 + right_string_length)
            
        return ans

