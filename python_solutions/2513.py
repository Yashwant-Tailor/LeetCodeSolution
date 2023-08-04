class Solution:
    def is_eq_satisfy(self,sol,divisor,cnt):
        return (sol - (sol//divisor)) >= cnt

    def binary_search(self,divisor,cnt):
        min_sol = 0
        max_sol = int(1e18)
        while min_sol + 1 < max_sol:
            mid_sol = min_sol + (max_sol - min_sol)//2
            if self.is_eq_satisfy(mid_sol,divisor,cnt):
                max_sol = mid_sol
            else:
                min_sol = mid_sol
        return max_sol

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # Solution Overview
        # we can take all integers except for the integers divisible by the lcm of divisor1,divisor2(because such integers won't fit in either arr1 or arr2) (in our solution we are making sure this thing by taking sol1)
        # also we need to make sure the maximum will be atleast the minimum required value for any array (in our solution we are making sure this thing by taking sol2 and sol3)
        from math import gcd
        gcd_of_div = gcd(divisor1,divisor2)
        lcm_of_div = (divisor1 * divisor2)//gcd_of_div
        
        sol1 = self.binary_search(lcm_of_div,uniqueCnt1+uniqueCnt2)
        sol2 = self.binary_search(divisor1,uniqueCnt1)
        sol3 = self.binary_search(divisor2,uniqueCnt2)
        return max([sol1,sol2,sol3])
