class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # solution Overview
       
        # when find a number i, flip the number at position i-1 to negative. 
        # if the number at position i-1 is already negative, i is the number that occurs twice.
        
        res = []
        for idx in range(len(nums)):
            curr_num = abs(nums[idx])
            loc = curr_num-1
            if nums[loc] < 0:
                res.append(curr_num)
            else:
                nums[loc] *= -1
        return res
    

        
