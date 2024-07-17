from typing import List, Optional


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
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        remaining = []
        self.toDelete = set(to_delete)

        if not root:
            return remaining

        def processRoot(
            root: Optional[TreeNode],
            parent: TreeNode,
            continuePrevious=False,
        ):
            if not root:
                return
            if root.val in self.toDelete:
                self.toDelete.remove(root.val)
                tmp = False
                if parent and parent.left and parent.left.val == root.val:
                    parent.left = None
                elif parent:
                    parent.right = None
            else:
                tmp = True
                if not continuePrevious:
                    remaining.append(root)

            processRoot(root.right, root, tmp)
            processRoot(root.left, root, tmp)

        processRoot(root, None)
        return remaining
