class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # Solution Overview
        # if all elements in the arrays are unique then answer would always be n-1
        # the optimal strategy in this case would be putting min elment in front of max elment for rest of the element we will put the element just greater than that number
        # now if we have repeated element than again the strategy will be same we just need to take in account the frequency of that particular element

        nums.sort()
        ans = 0 
        st = 0
        en = 0
        while en < len(nums):
            if nums[st] == nums[en]:
                en += 1
                continue
            ans += 1
            en += 1
            st += 1
        return ans

