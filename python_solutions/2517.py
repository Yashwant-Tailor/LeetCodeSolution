class Solution:
    def isPos(self,price,tastiness,k):
        prev_price = price[0]
        curr_idx = 1
        total_candies = 1
        while curr_idx < len(price):
            if price[curr_idx]-prev_price < tastiness:
                curr_idx += 1
            else:
                prev_price = price[curr_idx]
                curr_idx += 1
                total_candies += 1
        return total_candies >= k
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # Solution Overview
        # binary search for the maximum tastiness and for a given tastiness we can check in O(N) with that it is possible or not have that tastiness of a basket (we will sort the price and compute the candies which can be included with a particular tastiness)
        min_tastiness = 0
        max_tastiness = int(1e9+1)
        price.sort()
        while min_tastiness+1 < max_tastiness:
            mid_tastiness = min_tastiness + (max_tastiness - min_tastiness)//2
            if self.isPos(price,mid_tastiness,k):
                min_tastiness = mid_tastiness
            else:
                max_tastiness = mid_tastiness
        return min_tastiness
