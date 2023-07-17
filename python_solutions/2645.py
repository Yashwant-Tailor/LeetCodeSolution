class Solution:
    def addMinimum(self, word: str) -> int:
        # Solution Overview
        # consider a string in form of 'abcabc....abcabc' and compare the character of the input and this string if character is present then we don't need to add any extra character if character is not there we need to either 'a','b' or 'c'

        s = 'abc'
        idx = 0
        ans = 0
        for char in word:
            while s[idx] != char:
                ans += 1
                idx += 1
                idx %= 3
            idx += 1
            idx %= 3
        ans += (3-idx)%3
        return ans
