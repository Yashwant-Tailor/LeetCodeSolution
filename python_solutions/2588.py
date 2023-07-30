class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # Solution Overview
        # let's calculate the prefix bit sum i.e. prefix[i] = sum of bit in prefix till index i for each bit in 0 to 31 (as numbers are representable in 32 bit)
        # now if we look at the subarrays starting at index 0 , then it is clear that the end of such subarrays will be where we have prefix[i] having all the bit count as even
        # now to find the such end we acutally don't need to store the prefix it self
        # we can take help of even parity 
        # we will only store that the sum is having even parity or odd parity for each location (1 to 31)
        # again the sum is representable as a number so adding another number to the previous sum would be simple taking XOR with previous prefix sum

        curr_bit_sum = 0
        pre_bit_sum_count = {}
        for num in nums:
            curr_bit_sum ^= num
            if curr_bit_sum not in pre_bit_sum_count:
                pre_bit_sum_count[curr_bit_sum] = 1
            else:
                pre_bit_sum_count[curr_bit_sum] += 1
        ans = 0
        print(pre_bit_sum_count)
        for key,val in pre_bit_sum_count.items():
            ans += (val * (val-1))//2
            if key == 0:
                ans += val
        return ans

