// use queue then traverse using breadth first search
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
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*>st ; 
        st.push(root) ; 
        vector<int>v ; 
        bool ans = true ; 
        while(!st.empty() && ans){
            int sz = st.size() ;
            while(sz--){
                TreeNode* node  = st.front() ; 
                st.pop() ; 
                if(node->left != nullptr){
                    v.push_back(node->left->val) ; 
                    st.push(node->left) ; 
                }
                else{
                    v.push_back(101) ; 
                }
                if(node->right != nullptr){
                    v.push_back(node->right->val) ;
                    st.push(node->right) ;
                }
                else{
                    v.push_back(101) ;
                }
            }
            int i = 0 , j = v.size() -1 ;
            while(i < j){
                ans &= (v[i] == v[j]) ; 
                i++ ; j--;
            }
            v.clear() ;
        }
        return ans ; 
    }
};
