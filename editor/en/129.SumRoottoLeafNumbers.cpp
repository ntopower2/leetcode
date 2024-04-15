#include "iostream"
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int sumNumbers(TreeNode *root)
    {
        return visit(root, 0);
    }
    int visit(TreeNode *node, int total)
    {
        if (node == nullptr)
        {
            return 0;
        }
        total *= 10;
        total += node->val;

        if (node->left == nullptr && node->right == nullptr)
        {
            return total;
        }
        return visit(node->left, total) + visit(node->right, total);
    }
};

int main()
{
    TreeNode *s1 = new struct TreeNode(2);
    TreeNode *s2 = new struct TreeNode(3);
    TreeNode *s0 = new struct TreeNode(1, s1, s2);
    Solution s;
    cout << s.visit(s0, 0);
}