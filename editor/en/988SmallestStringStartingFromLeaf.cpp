#include "iostream"
#include <algorithm>
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
    string smallest;
    string smallestFromLeaf(TreeNode *root)
    {
        string tmp = "";
        dfs(root, tmp);
        return smallest;
    }

    void dfs(TreeNode *node, string &cur)
    {
        if (node == nullptr)
        {
            return;
        }
        cur += numToLetter(node->val);

        if (!node->left && !node->right)
        {
            string reversed = cur;
            reverse(reversed.begin(), reversed.end());

            if (smallest.empty() || reversed < smallest)
            {
                smallest = reversed;
            }
        }
        dfs(node->left, cur);
        dfs(node->right, cur);
        cur.pop_back();
    }

private:
    char numToLetter(int num)
    {
        return "abcdefghijklmnopqrstuvwxyz"[num];
    }
};

int main()
{
    TreeNode node5(3);
    TreeNode node51(3);
    TreeNode node1(4);
    TreeNode node11(4);
    TreeNode node2(1, &node5, &node1);
    TreeNode node6(2, &node51, &node11);
    TreeNode node4(0, &node2, &node6);

    Solution s;
    s.smallestFromLeaf(&node4);
}