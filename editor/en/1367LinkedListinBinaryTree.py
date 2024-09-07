# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNodesFromList(lst):
    nodes = [ListNode(lst[-1], None)]
    for i, num in enumerate(lst[::-1][1:]):
        nodes.append(ListNode(num, nodes[i]))

    return nodes[-1]


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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(curTreeNode: Optional[TreeNode], curListNode: Optional[ListNode]):
            if not curListNode:
                return True
            if not curTreeNode or curTreeNode.val != curListNode.val:
                return False

            return dfs(curTreeNode.left, curListNode.next) or dfs(
                curTreeNode.right, curListNode.next
            )

        if not root:
            return False
        return (
            dfs(root, head)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )


assert (
    Solution().isSubPath(
        createNodesFromList([4, 2, 8]),
        createTreeFrom(
            [1, 4, 4, None, 2, 2, None, None, None, 1, None, 6, 8, None, None]
        )[0],
    )
    == True
)
