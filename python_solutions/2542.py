class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Solution Overview
        # if we sort the nums2 array than for each min we can find the group of k-1 largest integer which will be included this element as minimum
        # finding the largest k-1 element can be done using heap

        import heapq as h
        min_heap = []
        arr = []
        for i in range(len(nums1)):
            arr.append((nums1[i],nums2[i]))
        arr.sort(key=lambda x : x[1])
        ans = 0
        curr_sum = 0
        for i in range(len(arr)-1,-1,-1):
            if len(min_heap) < k-1:
                h.heappush(min_heap,arr[i][0])
                curr_sum += arr[i][0]
                continue
            ans = max(ans , (curr_sum + arr[i][0])*arr[i][1])
            if k > 1 and arr[i][0] > min_heap[0]:
                curr_sum -= min_heap[0]
                h.heappop(min_heap)
                curr_sum += arr[i][0]
                h.heappush(min_heap,arr[i][0])
        return ans

            
