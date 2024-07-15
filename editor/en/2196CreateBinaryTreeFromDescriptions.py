# Definition for a binary tree node.
from typing import List, Optional
from collections import defaultdict
from random import randint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            self
            and other
            and self.val == other.val
            and self.left.__eq__(other.left)
            and self.right.__eq__(other.right)
        )


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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        parents = defaultdict(int)

        for p, c, l in descriptions:
            parents[c] = p
            nodes[p].val = p
            nodes[c].val = c
            if l:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

        x = randint(0, len(descriptions) - 1)
        p = descriptions[x][1]
        while parents[p]:
            p = parents[p]

        return nodes[p]


assert (
    Solution().createBinaryTree(
        [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
    )
    == createTreeFrom([50, 20, 80, 15, 17, 19])[0]
)
