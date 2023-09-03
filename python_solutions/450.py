# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_node_loc(self,node,key,parent = None):
        if node is None:
            return None,None
        if node.val == key:
            return node,parent
        return self.get_node_loc(node.left,key,node) if node.val > key else self.get_node_loc(node.right,key,node)
    def get_predecessor(self,node,parent):
        if node.left is None:
            return node,parent
        curr_node = node.left
        parent = node
        while curr_node.right is not None:
            next_node = curr_node.right
            parent = curr_node
            curr_node = next_node
        return curr_node,parent

    def delete_node(self,node,parent=None,prev_root = None):
        if node.left is None:
            if parent is None:
                new_root = node.right
                node.right = None
                return new_root
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            return prev_root
        pred_node,pred_parent = self.get_predecessor(node,parent)
        while pred_node != node:
            node.val,pred_node.val = pred_node.val,node.val
            node = pred_node
            parent = pred_parent
            pred_node,pred_parent = self.get_predecessor(node,parent)
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
        return prev_root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Solution Overview
        # first search for the node
        node_loc,parent_loc = self.get_node_loc(root,key)
        new_root = root
        if node_loc is not None :
            new_root = self.delete_node(node_loc,parent_loc,root)
        return new_root
        
