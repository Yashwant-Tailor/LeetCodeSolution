class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # Solution Overview
        # iteratively maintain the word[0...i] decimal representation and set the value for div[i] accordingly

        curr_dec_val = 0
        MOD = m
        div = []
        for char in word:
            curr_dec_val *= 10
            curr_dec_val %= MOD
            curr_dec_val += ord(char)-ord('0')
            curr_dec_val %= MOD
            if curr_dec_val == 0:
                div.append(1)
            else:
                div.append(0)
        return div
