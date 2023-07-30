class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Solution Overview
        # for first element pick the  prime number just small then the nums[0]
        # and substract it from nums[0]
        # from index > 1, calculate the difference nums[i]-nums[i-1] 
        # if this difference is greater then zero the find the prime number just smaller than this element and substract it from nums[i]
        # after performing all the operations if our array is sorted then return true otherwise return false

        just_small_prime = [-1 for i in range(1001)] # -1 denotes there is no prime just smaller then this number
        prev_prime = -1
        for i in range(2,1001):
            if just_small_prime[i] == -1:
                just_small_prime[i] = prev_prime
                prev_prime = i
                unmark_num = i*i
                while unmark_num < 1001:
                    just_small_prime[unmark_num] = 0 # just mark, not a prime
                    unmark_num += i
            else:
                just_small_prime[i] = prev_prime
        if just_small_prime[nums[0]] != -1:
            nums[0] -= just_small_prime[nums[0]]
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                if just_small_prime[diff] != -1:
                    nums[i] -= just_small_prime[diff]
            else:
                return False
        return True
                
