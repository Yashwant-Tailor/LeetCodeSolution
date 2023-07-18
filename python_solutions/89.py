class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Solution Overview
        # between every power of two we will try to place the number having same msb
        ans = [0]
        # iteratively build the ans
        for i in range(0,n):
            # we can take help of previously calculated ans array
            # as we know that ans is already satifying the quetions condition 
            # we need to add the number which is having their msb == i (i bit is the highest bit set in the numbers)
            # we can take the ans array , reverse it and set the ith msb and append it to ans array it will be correct answer for [0,2^i -1] 
            curr_arr = []
            for j in range(len(ans)-1,-1,-1):
                new_val = ans[j] | (1<<i)
                curr_arr.append(new_val)
            ans += curr_arr
        return ans

