class Solution:
    def isPos(self,nums,k):
        if 2*k <= len(nums):
            can_mark = True
            st = 0 
            en = len(nums)-k
            for i in range(k):
                can_mark &= (2*nums[i] <= nums[en+i])
            return can_mark
        return False
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        # Solution Oveview
        # if we focus on the binary representation of the nums[i]
        # then it is clear we can only pick i,j if nums[j] is having the msb greater than the nums[i]
        # let say that in our final answer we have (i,j) pairs(count = k) of indices 
        # then answer would be 2*k
        # if we look at the (nums[i],nums[j]) for all the k pairs in sorted order according to nums[i], then it is clear that in this sorted order i1 < i2 
        # then we have nums[i1] < num[i2] and nums[j1] < nums[j2]
        # again to pick maximize the value of k , it is optimal to pick the first smallest k elements as i indices and first k maximum element as j indices
        #
        # for a fix k we can perform the above check in O(N) time
        # Now to find the maximum value of k we can use the binary search and update the k accordingly
        nums.sort()
        k_st = 0
        k_en = len(nums)
        while k_st+1 < k_en:
            mid = k_st + (k_en - k_st)//2
            print(mid)
            if self.isPos(nums,mid):
                k_st = mid
            else:
                k_en = mid
        return 2 * k_st
