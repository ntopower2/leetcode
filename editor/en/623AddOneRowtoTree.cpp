#include "iostream"
#include "queue"
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
    TreeNode *addOneRow(TreeNode *root, int val, int depth)
    {
        if (depth == 1)
        {
            return new TreeNode(val, root, nullptr);
        }
        std::queue<TreeNode *> q;
        int d = 1;
        q.push(root);

        while (!q.empty())
        {
            int n = q.size();
            for (int i = 0; i < n; ++i)
            {
                TreeNode *node = q.front();
                q.pop();
                if (d == depth - 1)
                {
                    TreeNode *newLeftNode = new TreeNode(val, node->left, nullptr);
                    TreeNode *newRightNode = new TreeNode(val, nullptr, node->right);
                    node->left = newLeftNode;
                    node->right = newRightNode;
                }
                else
                {
                    if (node->left != nullptr)
                    {
                        q.push(node->left);
                    }

                    if (node->right != nullptr)
                    {
                        q.push(node->right);
                    }
                }
            }

            if (++d == depth)
            {
                return root;
            }
        }
        return nullptr;
    }
};

int main()
{
    TreeNode node5(5);
    TreeNode node1(1);
    TreeNode node3(3);
    TreeNode node2(2, &node3, &node1);
    TreeNode node6(6, &node5, nullptr);
    TreeNode node4(4, &node2, &node6);

    Solution s;
    cout << s.addOneRow(&node4, 1, 2);
}