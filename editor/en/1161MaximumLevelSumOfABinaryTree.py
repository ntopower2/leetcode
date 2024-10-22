#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = None
        current = [0, 0]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                current[1] += node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            current[0] += 1
            if res is None or current[1] > res[1]:
                res = current.copy()
            current[1] = 0

        return res[0]


# @lc code=end
assert Solution().maxLevelSum(createTreeFrom([-1, -1, 1, 0, 0])[0]) == 2
assert Solution().maxLevelSum(createTreeFrom([1, 7, 0, 7, -8, None, None])[0]) == 2
