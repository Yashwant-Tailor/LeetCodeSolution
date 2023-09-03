class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Solution Overview
        # if we sort every element then we will know about the final index where this element should be placed
        # if we have equal element then we will sort based on their index in given array, element with higher index will come after element with lower index
        # now to find a chunk we will find the maximum index in our iteration , and if this maximum index is equal to our current iteration index then we have one chunk 
        new_arr = []
        for idx,num in enumerate(arr):
            new_arr.append((num,idx))
        new_arr.sort(key=lambda x : (x[0],x[1]))
        chunk_count = 0
        idx = 0 
        max_id = -1
        while idx < len(new_arr):
            max_id = max(max_id,new_arr[idx][1])
            if max_id == idx:
                chunk_count += 1
                max_id = -1
            idx += 1
        return chunk_count
