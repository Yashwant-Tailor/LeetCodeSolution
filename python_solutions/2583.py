# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Solution Overview
        # perform the binary search and maintain a priority queue of size k to keep track of k larget value of level sum
        from collections import deque
        node_queue = deque()
        node_queue.append(root)
        import heapq as hp
        min_heap = []
        while len(node_queue) > 0:
            curr_level_elm_count = len(node_queue)
            level_sum = 0
            while curr_level_elm_count > 0:
                curr_level_elm_count -= 1
                curr_node = node_queue.popleft()
                if curr_node.left is not None:
                    node_queue.append(curr_node.left)
                if curr_node.right is not None:
                    node_queue.append(curr_node.right)
                level_sum += curr_node.val
            if len(min_heap) < k:
                hp.heappush(min_heap,level_sum)
            elif min_heap[0] < level_sum:
                hp.heappop(min_heap)
                hp.heappush(min_heap,level_sum)
        return min_heap[0] if len(min_heap) == k else -1
