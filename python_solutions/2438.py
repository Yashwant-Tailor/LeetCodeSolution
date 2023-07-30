class Solution:
    def get_inv(self,a,n,MOD):
        ans = 1
        curr_ap = a
        while n > 0:
            if n & 1:
                ans *= curr_ap
                ans %= MOD
            curr_ap *= curr_ap
            curr_ap %= MOD
            n >>= 1
        return ans

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Solution Overview
        # find the powers array (binary representation of n)
        # find the prefix array of product and then calculate the product for each query
        # product [li,ri] = prefix_prod[ri+1]/prefix_prod[li]
        # which is equivalent to product[li,ri] = prefix_prod[ri+1] * inv_prefix_prod[li] (taking the inverse of prefix_prod[li])

        powers = []
        curr_2p = 1
        MOD = int(1e9+7)
        while curr_2p <= n:
            if n & curr_2p :
                powers.append(curr_2p%MOD)
            curr_2p <<= 1
        prefix_prod = [1]
        for power in powers:
            curr_prod = (prefix_prod[-1]*power)%MOD
            prefix_prod.append(curr_prod)
        inv_prefix_prod = []
        for prod in prefix_prod:
            inv_prefix_prod.append(self.get_inv(prod,MOD-2,MOD))
        answer = []
        for query in queries:
            li , ri = query
            answer_i = ((prefix_prod[ri+1]%MOD) * (inv_prefix_prod[li]%MOD))%MOD
            answer.append(answer_i)
        return answer

