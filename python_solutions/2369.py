class Solution:
    def isValidParLen2(self,partn):
        return (len(partn) == 2 ) and (partn[0] == partn[1])
    def isValidParLen3(self,partn):
        return (len(partn) == 3) and ((partn[0] == partn[1] == partn[2]) or ((partn[0] == partn[1]-1) and (partn[0] == partn[2]-2)))

    def validPartition(self, nums: List[int]) -> bool:
        # Solution Overview
        # it is easy to see that size 2 or 3 array or good partition or not (we will simply check the three condition and if the array follows these condition then we done)
        # now let's say dp[i] = True/False (if we can partition our array till index i)
        # to calculate dp[i] , we will take help of dp[i-2] and dp[i-3]
        third_last_st = True # third index last state
        second_last_st = True # second index last state
        last_st = True # last index state
        curr_st = False # current index state
        for idx in range(len(nums)):
            if idx > 0 and self.isValidParLen2(nums[idx-1:idx+1]):
                curr_st |= second_last_st
            if idx > 1 and self.isValidParLen3(nums[idx-2:idx+1]):
                curr_st |= third_last_st
            third_last_st = second_last_st
            second_last_st = last_st
            last_st = curr_st
            curr_st = False
        return last_st

