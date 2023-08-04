class Solution:
    def __init__(self):
        self.primes = []
        self.all_prime_factors = set()
    def set_primes(self):
        vis = [True for i in range(1001)]
        vis[0] = False
        vis[1] = False
        for i in range(2,1001):
            if vis[i]:
                self.primes.append(i)
                for j in range(i*i,1001,i):
                    vis[j] = False
    def update_prime_factors(self,num):
        curr_idx = 0
        while num > 1:
            curr_prime = self.primes[curr_idx]
            if num%curr_prime == 0:
                self.all_prime_factors.add(curr_prime)
                while num%curr_prime == 0:
                    num //= curr_prime
            curr_idx += 1
        
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # Solution Overview
        # for each number find the prime factor and maintain a hashmap to keep track of unique prime factor in overall array

        self.set_primes()
        for num in nums:
            self.update_prime_factors(num)
        return len(self.all_prime_factors)

