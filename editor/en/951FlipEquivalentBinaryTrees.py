#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None:
            return root2 is None
        if root2 is None:
            return root1 is None
        if root1.val != root2.val:
            return False

        levels1 = deque([root1])
        levels2 = deque([root2])

        while levels1 and levels2:
            if len(levels1) != len(levels2):
                return False

            for _ in range(len(levels1)):
                node1 = levels1.popleft()
                node2 = levels2.popleft()

                # ensure that the left node exists
                if node1.left is None and node1.right is None:
                    if node2.left is not None or node2.right is not None:
                        return False
                elif node1.right is not None:
                    node1.left, node1.right = node1.right, node1.left

                # other left does not match
                if node2.left is not None and node2.left.val != node1.left.val:
                    # try with other right
                    if node2.right is not None:
                        if node2.right.val == node1.left.val:
                            node2.right, node2.left = node2.left, node2.right
                            if node1.right is not None and (
                                node2.right is None
                                or node2.right.val != node1.right.val
                            ):
                                return False
                        else:
                            return False
                    else:
                        return False

                if node1.left is not None:
                    levels1.append(node1.left)
                if node1.right is not None:
                    levels1.append(node1.right)
                if node2.left is not None:
                    levels2.append(node2.left)
                if node2.right is not None:
                    levels2.append(node2.right)

        return True


# @lc code=end

assert (
    Solution().flipEquiv(
        createTreeFrom([6, 1, 0])[0],
        createTreeFrom([6, None, 1])[0],
    )
    == True
)
