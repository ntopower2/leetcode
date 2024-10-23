#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# class TreeNode:
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        parent = {root.val: root.val}

        while queue:
            xFound = x in parent
            yFound = y in parent
            if xFound and yFound:
                return parent[x] != parent[y]
            elif xFound or yFound:
                return False
            parent = {}
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parent[node.left.val] = node.val
                if node.right:
                    queue.append(node.right)
                    parent[node.right.val] = node.val


# @lc code=end


assert (
    Solution().isCousins(createTreeFrom([1, 2, 3, 4, None, 5, None])[0], 4, 5) == True
)
