// simple use depth first search (recursion) or breadth first search (queue)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if( root == nullptr){
            return 0 ; 
        }
        queue<TreeNode*>q ; 
        int depth = 0 ; 
        q.push(root) ; 
        while(!q.empty()){
            depth++ ;
            int sz = q.size() ; 
            while(sz--){
                TreeNode* node = q.front()  ;
                q.pop() ; 
                if(node->left != nullptr){
                    q.push(node->left) ;
                }
                if(node->right != nullptr){
                    q.push(node->right) ;
                }
            }
        }
        return depth ; 
    }
};
