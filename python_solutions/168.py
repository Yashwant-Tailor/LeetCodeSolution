class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Solution Overview
        final_str = ''
        curr_p = 26
        while columnNumber > 0:
            columnNumber -= 1
            final_str = chr(columnNumber%26 + ord('A')) + final_str
            columnNumber //= 26
        return final_str

