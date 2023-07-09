// inorder [left , root , right]
// preorder [root , left , right] 
// use preorder to make root
// because value are unique 
// find out the root in inorder 
// call for left subtree
// call for right subtree
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
    TreeNode* makeTree(vector<int>&preorder , vector<int>&inorder , int indPre , int l , int r){
        if(l > r){
            return nullptr ; 
        }
        TreeNode * node = new TreeNode ; 
        node->val = preorder[indPre] ; 
        int node_ind  ; 
        int count =  0 ;
        for(int i = l ; i <= r ; i++){
            if(inorder[i] == preorder[indPre]){
                node_ind = i ; 
                break;
            }
            else{
                count++ ; 
            }
        }
        
        node->left  = makeTree(preorder , inorder , indPre + 1 , l , node_ind -1) ; 
        node->right = makeTree(preorder , inorder , indPre + count+1, node_ind+1 , r) ; 
        return node ; 
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int indPre = 0 , l = 0 , r = inorder.size() -1 ;
        return makeTree(preorder , inorder , indPre , l , r) ;
    }
};
