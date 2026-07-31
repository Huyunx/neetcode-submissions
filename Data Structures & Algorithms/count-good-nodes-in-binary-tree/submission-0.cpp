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
private:
    int ans(TreeNode* node, int maxvalue){
        if(node == nullptr){
            return 0;
        }
        int add=0;
        if(node->val>= maxvalue){
            add=1;
        }
     
        return add+ans(node->left,max(node->val,maxvalue)) + ans (node->right,max(node->val,maxvalue));
    }
public:
    int goodNodes(TreeNode* root) {
        return ans(root,root->val);
    }
};
