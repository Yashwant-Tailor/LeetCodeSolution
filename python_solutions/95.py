# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def get_all_subtree(self,node_val):
        if len(node_val) == 0:
            return [None]
        res = []
        for i in range(len(node_val)):
            left_subtree = self.get_all_subtree(node_val[:i])
            right_subtree = self.get_all_subtree(node_val[i+1:])
            for left_s in left_subtree:
                for right_s in right_subtree:
                    curr_bst_root = TreeNode(node_val[i],left_s,right_s)
                    res.append(curr_bst_root)
        return res
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Solution Overview
        # recursively build the tree for by dividing the node_val array in three part 
        # let's say we have the three indices which decides the boundaries of node_val (i,j,k)
        # build all left subtree for [i,j) 
        # build all right subtree for (j,k]
        # build all tree but making root node as j
        node_val = [i for i in range(1,n+1)]
        return self.get_all_subtree(node_val)
