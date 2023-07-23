class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Solution Overview
        # if we sort the array then it is clear that max value will abs(nums[0]-nums[len(nums)-1])
        # minimum value in sorted array would minimum value of abs(nums[i]-nums[i+1]) where  0 <= i < len(nums)-1
        # CASE1 : it would be optimal to minimize the score that we change the nums[0] and nums[1] in the sorted array to nums[2] 
        # in this way minimum value will be 0 and maximum value will get reduced as well
        # CASE2 : or we apply the same operation in reverse order
        # CASE3 : or we apply one operation on one end and other operation on another end of sorted array
        nums.sort()
        # CASE1
        ans1 = abs(nums[-1]-nums[2])
        # CASE2
        ans2 = abs(nums[-3]-nums[0])
        # CASE3
        ans3 = abs(nums[1] - nums[-2])
        return min([ans1,ans2,ans3])
