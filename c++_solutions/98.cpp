// simple recursion 
// hint : return the maximum and minimum of left and right binary tree of the current node and compare this values with current node value
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
    pair<int,int> isBST(TreeNode*root , bool & ans){
        if((root->left != nullptr) && (root->right != nullptr)){
            pair<int,int>a , b ; 
            a = isBST(root->left ,ans) ;
            b = isBST(root->right , ans) ;
            ans &= (max(a.first , a.second) < root->val && min(b.first , b.second) > root->val) ;
            int ma = max(a.first  , max(a.second , max(b.first  , max(b.second , root->val)))) ; 
            int mi = min(a.first  , min(a.second , min(b.first  , min(b.second , root->val)))) ; 
            return make_pair(mi , ma) ; 
        }
        else if(root->left != nullptr){
            pair<int,int>a = isBST(root->left , ans ) ; 
            ans &= (max(a.first , a.second) < root->val) ; 
            int ma = max(a.first , max(a.second , root->val)) ;
            int mi = min(a.first , min(a.second , root->val)) ;
            return make_pair(ma , mi) ;
        }
        else if(root->right != nullptr){
            pair<int,int>a = isBST(root->right , ans) ; 
            ans &= (min(a.first , a.second) > root->val) ; 
            int ma = max(a.first , max(a.second , root->val)) ;
            int mi = min(a.first , min(a.second , root->val)) ;
            return make_pair(ma , mi) ;
        }
        else{
            return make_pair(root->val , root->val) ;
        }
        return make_pair(root->val , root->val) ;
    }
    bool isValidBST(TreeNode* root) {
        bool ans = true ; 
        if(root == nullptr){
            return ans ; 
        }
        isBST(root , ans) ; 
        
        return ans ; 
    }
};
