from itertools import zip_longest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        a_gen = self._get_leaf_values(root1)
        b_gen = self._get_leaf_values(root2)
        while True:
            try:
                a = next(a_gen)
            except StopIteration:
                try:
                    next(b_gen)
                except StopIteration:
                    return True
                return False
            try:
                b = next(b_gen)
            except StopIteration:
                return False
            if a != b:
                return False

    def _get_leaf_values(self, root: TreeNode):
        if root.left is not None:
            yield from self._get_leaf_values(root.left)
        if root.right is not None:
            yield from self._get_leaf_values(root.right)
        if root.left is None and root.right is None:
            yield root.val


# tree_1_1 = TreeNode(9)
# tree_1_2 = TreeNode(8)
# tree_1_3 = TreeNode(5)
# tree_1_4 = TreeNode(1, left=tree_1_1, right=tree_1_2)
# tree_1_5 = TreeNode(3, left=tree_1_3, right=tree_1_4)
#
# tree_2_1 = TreeNode(5)
# tree_2_2 = TreeNode(9)
# tree_2_3 = TreeNode(1, left=tree_2_1, right=tree_2_2)
# tree_2_4 = TreeNode(8)
# tree_2_5 = TreeNode(3, left=tree_2_3, right=tree_2_4)
#
#
# sol = Solution()
# print(sol.leafSimilar(tree_1_5, tree_2_5))
