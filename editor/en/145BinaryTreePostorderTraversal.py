from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTreeFrom(nodes: List[int]) -> TreeNode:
    treeNodes = [None] * len(nodes)
    treeNodes[0] = TreeNode(nodes[0])
    for i, node in enumerate(nodes):
        if node is not None and i > 0:
            treeNodes[i] = TreeNode(node)
            if i % 2:
                treeNodes[(i - 1) // 2].left = treeNodes[i]
            else:
                treeNodes[(i - 1) // 2].right = treeNodes[i]
    return treeNodes


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res += [root.val]

        return res


assert Solution().postorderTraversal(
    createTreeFrom([1, None, 2, None, None, 3])[0]
) == [
    3,
    2,
    1,
]
