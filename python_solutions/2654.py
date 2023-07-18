class Solution:
    def get_gcd(self,num1,num2):
        if num1 < num2:
            num1 , num2 = num2, num1
        if num2 == 0:
            return num1
        return self.get_gcd(num2,num1%num2)
    def minOperations(self, nums: List[int]) -> int:
        # Solution Overview
        # all elements will be equal to after some operations if the gcd of all elements of the array nums is equal to 1
        # if possible to make all the elements equal to 1 , then the number of operations would be the group of contigous elements which has gcd equal to 1. we will apply the operation on this group and we will have 1 in the array from there onward we can take adjacent element to 1 to make these elements equal to 1.

        is_possible = True
        gcd = nums[0]
        for i in range(1,len(nums)):
            gcd = self.get_gcd(gcd,nums[i])
        if gcd != 1:
            return -1
        ans = 0
        group_left_ind = 0
        group_right_ind = len(nums)-1
        for i in range(len(nums)):
            curr_left_ind = i
            curr_right_ind = i
            gcd = nums[i]
            while curr_right_ind < len(nums):
                gcd = self.get_gcd(gcd,nums[curr_right_ind])
                if gcd == 1:
                    break
                curr_right_ind += 1
            if gcd == 1 and abs(curr_right_ind - curr_left_ind) < abs(group_left_ind - group_right_ind):
                group_right_ind = curr_right_ind
                group_left_ind = curr_left_ind
        # perform the operation in this group to get 1 in the array
        for i in range(group_left_ind+1,group_right_ind+1):
            nums[i] = self.get_gcd(nums[i],nums[i-1])
            ans += 1
        # with the help of the 1 make all elements equal to 1
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            ans += 1
        return ans


