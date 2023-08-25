class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Solution Overview
        # if we do similar to binary serach
        # then we can have following cases
        # CASE1 : mid-1 < mid > mid+1
        #       mid : mid is grater then both its neighbour i.e. mid is the peak , then just return mid
        # CASE2 : mid < mid+1
        #       then we know for sure that there will be atleast one peak in right side , as we have nums[n] = -negative infinity
        # CASE3 : mid-1 > mid
        #       then we know for sure that there will be atleast one peak in left side, as we have nums[0] = -negative infinity

        left_idx = 0
        right_idx = len(nums)-1
        while left_idx <= right_idx :
            mid_idx = left_idx + (right_idx - left_idx)//2
            if mid_idx == left_idx:
                if nums[left_idx] < nums[right_idx] :
                    return right_idx
                return left_idx
            if (nums[mid_idx-1] < nums[mid_idx])  and (nums[mid_idx] > nums[mid_idx+1]):
                return mid_idx
            if nums[mid_idx-1] > nums[mid_idx] :
                right_idx = mid_idx
            else:
                left_idx = mid_idx
