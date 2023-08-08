class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution Overview
        # we can think of performing the normal binary search with little bit of modification
        # in normal binary serach we divide the interval into two parts
        # [min,mid] and [mid,max]
        # in our modified binary serach first we will check that which interval is in inscreasing order
        # let's assume without loss of generality that [min,mid] is in increasing order
        # now we will try to discard either this interval or [mid,max] interval based on in which interval we have our target ( which we can find easily by comparing the value in nums[min] and nums[mid] with the target)
        # for more details please see the solution
        min_idx = 0
        max_idx = len(nums)-1
        while min_idx <= max_idx:
            mid_idx = min_idx + (max_idx - min_idx)//2
            if nums[mid_idx] == target:
                return mid_idx
            if nums[mid_idx] < nums[max_idx]:
                if target > nums[mid_idx] and target <= nums[max_idx]:
                    min_idx = mid_idx + 1
                else:
                    max_idx = mid_idx - 1
            else:
                if target >= nums[min_idx] and target < nums[mid_idx]:
                    max_idx = mid_idx - 1
                else:
                    min_idx = mid_idx + 1
        return -1
        
