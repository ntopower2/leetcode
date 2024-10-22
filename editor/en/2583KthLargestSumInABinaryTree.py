#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
from heapq import heappush, heappop, heapreplace


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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        levelSums = [0] * k
        queue = deque([root])
        while queue:
            tmp = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                tmp += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(levelSums) < k:
                heappush(levelSums, tmp)
            elif tmp > levelSums[0]:
                heapreplace(levelSums, tmp)

        if len(levelSums) < k or not levelSums[0]:
            return -1

        return levelSums[0]


# @lc code=end

assert (
    Solution().kthLargestLevelSum(createTreeFrom([5, 8, 9, 2, 1, 3, 7, 4, 6])[0], 2)
    == 13
)
