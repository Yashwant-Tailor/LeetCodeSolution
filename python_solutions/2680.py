class Solution:
    def get_num_msb(self,num):
        msb = 31
        while num & (1<<msb) == 0:
            msb -= 1
        return msb
    def maximumOr(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # multiplying with 2 is same as shifting the bit by one position in left direction (i.e. if we multiply n with 2 then it is equivalent to say n << 1)
        # Optimal strategy to make the final OR result maximum , would be apply all operations on the number which has highest MSB set (if we have multiple such numbers then check for each one)

        
        msb = 0
        for num in nums:
            msb = max(msb , self.get_num_msb(num))

        non_msb_num_or = 0
        msb_num_or = 0
        msb_num = [] # keep track of numbers which has msb set
        bit_count = [0 for i in range(32)] # keep track of bit count in numbers which has msb set
        for num in nums:
            if num & (1<<msb):
                msb_num.append(num)
                for i in range(32):
                    if num & (1<<i):
                        bit_count[i] += 1
                msb_num_or |= num
            else:
                non_msb_num_or |= num
        ans = 0
        for num in msb_num:
            # if we apply all k operations on this num
            # if for some bit location we have bit_count == 1 then it is only set in num so we need to remove this bit from bit_count and 
            curr_msb_num_or = msb_num_or
            for i in range(32):
                if num & (1<<i) and bit_count[i] == 1:
                    curr_msb_num_or ^= (1<<i)
            curr_ans = non_msb_num_or | curr_msb_num_or | (num << k)
            ans = max(ans,curr_ans)
        return ans
