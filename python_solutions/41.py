class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        curr_idx = 0 
        while curr_idx < len(nums):
            while 0 <= nums[curr_idx]-1 < len(nums) and nums[curr_idx] != nums[nums[curr_idx]-1]:
                tmp_num = nums[curr_idx]
                nums[curr_idx] = nums[tmp_num-1]
                nums[tmp_num-1] = tmp_num
            curr_idx += 1
        curr_idx = 0
        while curr_idx < len(nums):
            if curr_idx+1 != nums[curr_idx]:
                return curr_idx+1
            curr_idx += 1
        return curr_idx+1
