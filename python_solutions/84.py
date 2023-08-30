class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Solution Overview
        # Very classic problem , to use the stack (MONOTONIC STACK)
        # lets say we have choose n histogram bars to form the rectable , then it is always optimal to choose the lenght of the reactable equal to the minimum length out of n histogram bars
        # now if we index i as minimum length histogram bar , then we need to find the left and right boundaries till this index will be minimum (once we have index we can calculate the area of the reactangle)
        # we can take help of MONOTONIC STACK to find the left and right index which are just smaller then the given index

        left_idx = []
        idx_stack = []
        for idx,height in enumerate(heights):
            while len(idx_stack) > 0 and height <= heights[idx_stack[-1]]:
                idx_stack.pop()
            if len(idx_stack) == 0:
                left_idx.append(0)
            else:
                left_idx.append(idx_stack[-1]+1)
            idx_stack.append(idx)
        idx_stack.clear()
        largest_area = -1
        for idx in range(len(heights)-1,-1,-1):
            height = heights[idx]
            while len(idx_stack) > 0 and height <= heights[idx_stack[-1]]:
                idx_stack.pop()
            if len(idx_stack) == 0:
                right_idx = len(heights)-1
            else:
                right_idx = idx_stack[-1]-1
            idx_stack.append(idx)
            width = right_idx - left_idx[idx] + 1
            largest_area = max(largest_area, width * height)
        return largest_area
