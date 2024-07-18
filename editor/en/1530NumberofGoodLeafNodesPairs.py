from collections import defaultdict
from typing import List


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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        if not root:
            return 0

        def dfs(s: TreeNode, depth: int, leafDepthCounts: defaultdict):
            if not s or depth >= distance:
                return
            if not s.left and not s.right:
                leafDepthCounts[depth] += 1
                return
            dfs(s.left, depth + 1, leafDepthCounts)
            dfs(s.right, depth + 1, leafDepthCounts)

        res = self.countPairs(root.left, distance) + self.countPairs(
            root.right, distance
        )

        leafDepthCountsL = defaultdict(int)
        leafDepthCountsR = defaultdict(int)
        dfs(root.left, 1, leafDepthCountsL)
        dfs(root.right, 1, leafDepthCountsR)

        for i, dl in leafDepthCountsL.items():
            for j, dr in leafDepthCountsR.items():
                if i + j <= distance:
                    res += dl * dr

        return res


assert Solution().countPairs(createTreeFrom(list(range(1, 8)))[0], 3) == 2
