# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Solution Overview
        # walk through the tree depth wise 
        # maintain a list of parents (initially empty)
        # for all parent find the sum of all siblings value
        # for a particular parent update it accodingly

        root.val = 0
        parents = [root]
        while len(parents) > 0:
            # for all the parents calculate their child sum
            total_child_sum = 0
            for parent in parents:
                if parent.left is not None:
                    total_child_sum += parent.left.val
                if parent.right is not None:
                    total_child_sum += parent.right.val
            children = []
            for parent in parents:
                left_child = parent.left
                right_child = parent.right
                # for each parent the sum of its child value
                child_val_sum  = 0
                if left_child is not None :
                    child_val_sum += left_child.val
                if right_child is not None:
                    child_val_sum += right_child.val
                # add the children to child list with updated value
                if left_child is not None:
                    left_child.val = total_child_sum - child_val_sum
                    children.append(left_child)
                if right_child is not None:
                    right_child.val = total_child_sum - child_val_sum
                    children.append(right_child)
            # now these children will be next parents for which we will do the same calculation as we did above
            parents = children
        return root
