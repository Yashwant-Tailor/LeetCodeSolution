class Solution:
    def is_vowel(self,char):
        return char in ['a','e','i','o','u']

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Solution Overview
        # use prefix sum to find the count of string in given range which starts and ends with vowels

        pre_sum = [0]
        for word in words:
            curr_sum = pre_sum[-1]
            if self.is_vowel(word[0]) and self.is_vowel(word[-1]):
                curr_sum += 1
            pre_sum.append(curr_sum)
        ans = []
        for query in queries:
            li,ri = query
            ansi = pre_sum[ri+1] - pre_sum[li]
            ans.append(ansi)
        return ans
