class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # Solution Overview
        # if we look at the last element , then it is not optimal to apply any operation on this number , as it will decrease the overall value on this place , and it might lead to perform more operations in left side of this index
        # now using this fact we can optimallly decrease the value of second last element , and whatever minimum value we left with will help us in replacing the third last element .....so on.
        op = 0
        prev_num = nums[-1]
        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] <= prev_num:
                prev_num = nums[idx]
            else:
                op_cnt = (nums[idx]+prev_num-1)//prev_num
                prev_num = nums[idx]//op_cnt
                op += op_cnt - 1
        return op
