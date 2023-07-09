// postorder [left , right , root]
// inorder [left , root , right]
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
    TreeNode* makeTree(vector<int>&inorder , vector<int>&postorder , int postInd , int  l , int r){
        if(l > r){
            return nullptr ; 
        }
        TreeNode* node = new TreeNode ; 
        node->val = postorder[postInd] ; 
        int  node_ind; 
        for(int  i = l ; i <= r ; i++){
            if(inorder[i] == node->val){
                node_ind =  i ; 
                break ; 
            }
        }
        node->left = makeTree(inorder , postorder , postInd- (r - node_ind + 1) , l , node_ind-1 ) ; 
        node->right = makeTree(inorder , postorder ,  postInd - 1 , node_ind+1  , r) ; 
        return node ; 
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int postInd = postorder.size() -1  , l = 0 , r = inorder.size() -1 ;
        return makeTree(inorder , postorder , postInd , l , r) ; 
    }
};
