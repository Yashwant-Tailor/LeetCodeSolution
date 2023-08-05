class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # Solution Overview
        # the idea is to find the answer for each bit separately 
        # as per given constraint in the problem we will at most have 32 bit in any number
        # for each bit we will calculate that this bit will be set or unset in the final answer
        # as we know that XORing odd number of bits will result in 1 and even number results in 0
        # so if in our final answer the ith bit will be set if we have all the tripltes (i,j,k) count odd , where we have ith bit set
        # for a triplet the ith bit will be set if and only if ith bit of nums[k] is set and ith bit of (either nums[i] or nums[j]) is set
        # we can calculate this very easily check the solution how to effectively find count of triplets where we have ith bit set

        ans = 0
        for i in range(32):
            set_bit_count = 0
            unset_bit_count = 0
            for num in nums:
                if num & (1<<i):
                    set_bit_count += 1
                else:
                    unset_bit_count += 1
            choices_to_pick_k = set_bit_count
            choices_to_pick_i_and_j = (set_bit_count * unset_bit_count) * 2 + (set_bit_count *   set_bit_count)
            total_triplet_count = choices_to_pick_k * choices_to_pick_i_and_j
            if total_triplet_count%2:
                ans |= (1<<i)
        return ans
