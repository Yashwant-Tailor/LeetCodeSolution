class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Solution Overview
        # if array was sorted (not rotated) then we can simply use binary search to find the element
        # but in our problem we have array rotated 
        # now if we go the same idea as binary search then we first fix the mid index then try to discard one half base on the value 
        # also we can notice that in our given sorted roated array if we fix mid index then there always will be an interval (either left or right) , which will be either decreasing or increasing 
        # using this fact we can discard one half and find that target is there or not
        # we need to specially handle the case when our mid index element is equal to left and right index element
        # to handle this case we will check that if our elements are equal in one half then we will just discard that half (see the solution for more information)
        left_idx = 0
        right_idx = len(nums)-1
        while left_idx <= right_idx :
            mid_idx = left_idx + (right_idx - left_idx)//2
            if nums[mid_idx] == target:
                return True
            if nums[left_idx] == nums[mid_idx] == nums[right_idx]:
                is_all_same = True
                val = nums[mid_idx]
                for idx in range(left_idx,mid_idx+1):
                    is_all_same &= (nums[idx] == val)
                if is_all_same:
                    left_idx = mid_idx + 1
                else:
                    right_idx = mid_idx - 1 
            else:
                if nums[mid_idx] <= nums[right_idx]:
                    if nums[mid_idx]<= target <= nums[right_idx]:
                        left_idx = mid_idx + 1
                    else:
                        right_idx = mid_idx - 1
                else:
                    if nums[left_idx] <= target <= nums[mid_idx]:
                        right_idx = mid_idx - 1
                    else:
                        left_idx = mid_idx + 1
        return False
