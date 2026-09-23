"""
LeetCode 226: Invert Binary Tree (Easy)
Патерн: Tree / DFS (Рекурсивне віддзеркалення)
Час: O(n), Пам'ять: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # Міняємо місцями ліве і праве піддерево
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    sol = Solution()
    # Дерево: 4 -> (2, 7)
    r = TreeNode(4, TreeNode(2), TreeNode(7))
    inv = sol.invertTree(r)
    print("Test 1:", inv.val, inv.left.val, inv.right.val)  # 4, 7, 2
