class Solution:
    import random
    def find_kth_largest(self,nums,k,min_idx,max_idx):
        pivot_idx = random.randint(min_idx,max_idx)
        pivot_val = nums[pivot_idx]
        left_idx , mid_idx = min_idx-1,min_idx-1
        curr_idx = min_idx
        while curr_idx <= max_idx:
            if nums[curr_idx] == pivot_val:
                nums[mid_idx+1],nums[curr_idx] = nums[curr_idx],nums[mid_idx+1]
                mid_idx += 1
            elif nums[curr_idx] < pivot_val:
                nums[mid_idx+1],nums[curr_idx] = nums[curr_idx],nums[mid_idx+1]
                nums[left_idx+1],nums[mid_idx+1] = nums[mid_idx+1],nums[left_idx+1]
                mid_idx += 1
                left_idx += 1
            curr_idx += 1
        left_elm_cnt = left_idx+1 - min_idx
        eq_elm_cnt = mid_idx - left_idx
        right_elm_cnt = (max_idx - min_idx + 1) - (left_elm_cnt + eq_elm_cnt)
        if right_elm_cnt >= k:
            return self.find_kth_largest(nums,k,mid_idx+1,max_idx)
        elif right_elm_cnt+eq_elm_cnt >= k:
            return pivot_val
        else:
            return self.find_kth_largest(nums,k-(right_elm_cnt+eq_elm_cnt),min_idx,left_idx)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # we can use the idea of quicksort 
        # in quicksort we select a pivot and then divide the array into three partitions 
        # left partition contains the values which are lesser than the pivot 
        # mid partition contains the values equal to the pivot
        # right partition contains the values greater than the pivot
        # based on the value of k we can and the length of these partition we can select the right partition to search further our kth largest element

        min_idx = 0
        max_idx = len(nums)-1
        return self.find_kth_largest(nums,k,min_idx,max_idx)



