class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Solution Overview
        # we maintain a heap to keep track of possible pairs which can be first k smallest pairs
        # every time we pick a pair with minimum sum , we try to add the next possible pairs for smallest sum
        import heapq as hp
        min_sum_heap = []
        hp.heappush(min_sum_heap,(nums1[0]+nums2[0],(0,0)))
        ans = []
        taken_idx= set()
        while k > 0 and len(min_sum_heap) > 0:
            su,idx = hp.heappop(min_sum_heap)
            if idx in taken_idx:
                continue
            k -= 1
            idx1,idx2 = idx
            ans.append((nums1[idx1],nums2[idx2]))
            taken_idx.add(idx)
            if idx1 + 1 < len(nums1):
                hp.heappush(min_sum_heap,(nums1[idx1+1]+nums2[idx2],(idx1+1,idx2)))
            if idx2 + 1 < len(nums2):
                hp.heappush(min_sum_heap,(nums1[idx1]+nums2[idx2+1],(idx1,idx2+1)))
        return ans
