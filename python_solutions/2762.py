class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        # Solution Overview
        # calculate the index

        # maintain min heap and max heap to keep track of min and max value in current interval
        from dataclasses import dataclass, field
        @dataclass()
        class MinHeap_Elem:
            val: int = field(compare=True)

            def __eq__(self, other):
                return self.val == other.val

            def __lt__(self, other):
                return self.val <= other.val

        @dataclass()
        class MaxHeap_Elem:
            val: int = field(compare=True)

            def __eq__(self, other):
                return self.val == other.val

            def __lt__(self, other):
                return self.val >= other.val

        import heapq as hp
        min_heap = []
        elements_dict = {}
        max_heap = []
        ans = 0
        curr_left_end = 0
        for idx, num in enumerate(nums):
            if idx > 0:
                curr_min = min(num , min_heap[0].val)
                curr_max = max(num , max_heap[0].val)
                while len(min_heap) > 0 and len(max_heap) > 0 and abs(curr_max-curr_min)>2:
                    curr_left_end_num = nums[curr_left_end]
                    curr_left_end += 1
                    elements_dict[curr_left_end_num] -= 1
                    if elements_dict[curr_left_end_num] == 0:
                        elements_dict.pop(curr_left_end_num)
                    while len(min_heap)>0 and min_heap[0].val not in elements_dict:
                        hp.heappop(min_heap)
                    while len(max_heap) > 0 and max_heap[0].val not in elements_dict:
                        hp.heappop(max_heap)
                    if len(min_heap)>0:
                        curr_min = min(num, min_heap[0].val)
                        curr_max = max(num, max_heap[0].val)
            hp.heappush(min_heap, MinHeap_Elem(num))
            hp.heappush(max_heap, MaxHeap_Elem(num))
            ans += idx-curr_left_end+1
            if nums[idx] in elements_dict:
                elements_dict[nums[idx]] += 1
            else:
                elements_dict[nums[idx]] = 1
        return ans

