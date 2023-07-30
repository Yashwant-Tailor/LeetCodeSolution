class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Solution Overview
        # in the nums array if we have maximum m occurance of a number , then in our final matrix we will have m rows and now place the other numbers accordingly
        num_freq = {}
        max_freq = 0
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
            max_freq = max(max_freq,num_freq[num])
        ans = [[] for i in range(max_freq)]
        for num,freq in num_freq.items():
            idx = 0
            while freq > 0:
                ans[idx].append(num)
                idx += 1
                freq -= 1
        return ans
            
        
