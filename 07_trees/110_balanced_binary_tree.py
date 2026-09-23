"""
LeetCode 110: Balanced Binary Tree (Easy)
Pattern: Tree / DFS (Height Balanced Check)
Time: O(n), Space: O(h)
Idea: If the absolute height difference of left and right subtrees > 1, return -1 (unbalanced).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def check(node: TreeNode | None) -> int:
            if not node:
                return 0

            left_h = check(node.left)
            if left_h == -1:
                return -1

            right_h = check(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return 1 + max(left_h, right_h)

        return check(root) != -1


if __name__ == "__main__":
    sol = Solution()
    # Balanced: 3 -> 9, (20 -> 15, 7)
    t1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Test 1 Balanced:", sol.isBalanced(t1))  # True
