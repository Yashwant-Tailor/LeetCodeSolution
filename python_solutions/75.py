class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_sort_ind = 0
        # sort for red
        for idx,num in enumerate(nums):
            if num == 0:
                # swap this red object at index curr_sort_ind
                nums[curr_sort_ind],nums[idx] = nums[idx],nums[curr_sort_ind]
                curr_sort_ind += 1
        # sort for white
        for idx,num in enumerate(nums):
            if num == 1:
                # swap this white object at index curr_sort_ind
                nums[curr_sort_ind],nums[idx] = nums[idx],nums[curr_sort_ind]
                curr_sort_ind += 1
