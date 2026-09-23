"""
LeetCode 543: Diameter of Binary Tree (Easy)
Pattern: Tree / DFS (Diameter Calculation)
Time: O(n), Space: O(h)
Idea: Diameter through any node = left_height + right_height. Track the maximum across all nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        max_d = 0

        def height(node: TreeNode | None) -> int:
            nonlocal max_d
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # Update the longest path passing through this node
            max_d = max(max_d, left_h + right_h)

            return 1 + max(left_h, right_h)

        height(root)
        return max_d


if __name__ == "__main__":
    sol = Solution()
    # 1 -> (2 -> 4, 5), 3
    t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Test 1 Diameter:", sol.diameterOfBinaryTree(t))  # 3
