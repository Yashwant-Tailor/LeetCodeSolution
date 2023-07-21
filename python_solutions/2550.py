class Solution:
    def monkeyMove(self, n: int) -> int:
        # Solution Overview
        # each monkey has two choices either move clockwise or anti clockwise
        # so we have 2^n possible combination of movements of these monkeys
        # out of all combination of movements,we have only two combination (all monakey moves in clockwise or anticlockwise direction) where no mokey will collide
        # so the final answer would be 2^n - 2
        ans = 1
        MOD = int(1e9 + 7)
        curr_2p = 2
        while n > 0:
            if n & 1 > 0:
                ans *= curr_2p
                ans %= MOD
            curr_2p *= curr_2p
            curr_2p %= MOD
            n >>= 1
        return ((ans - 2)%MOD+MOD)%MOD
