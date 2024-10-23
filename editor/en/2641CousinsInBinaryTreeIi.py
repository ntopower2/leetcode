#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTreeFrom(nodes: List[int]) -> List[TreeNode]:
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        parent = {root: None}
        while queue:
            levelNodes = []
            tmp = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                levelNodes.append(node)
                tmp += node.val
                if node.right:
                    queue.append(node.right)
                    parent[node.right] = node
                if node.left:
                    queue.append(node.left)
                    parent[node.left] = node

            brotherNodes = []
            brotherSum = 0
            for node in levelNodes:
                if not brotherNodes or (
                    parent[brotherNodes[-1]]
                    and parent[brotherNodes[-1]] == parent[node]
                ):
                    brotherNodes.append(node)
                    brotherSum += node.val
                else:
                    for brother in brotherNodes:
                        brother.val = tmp - brotherSum
                    brotherNodes = [node]
                    brotherSum = node.val

            for brother in brotherNodes:
                brother.val = tmp - brotherSum

        return root


# @lc code=end
assert Solution().replaceValueInTree(createTreeFrom([5, 4, 9, 1, 10, None, 7])[0]) == [
    0,
    0,
    0,
    7,
    7,
    None,
    11,
]
