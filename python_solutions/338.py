class Solution:
    def get_1s(self,num):
        set_bit = 0
        while num > 0:
            if num & 1 :
                set_bit += 1
            num >>= 1
        return set_bit
    def countBits(self, n: int) -> List[int]:
        # Solution Overview
        ans = []
        for num in range(n+1):
            ans.append(self.get_1s(num))
        return ans

        
