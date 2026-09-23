"""
LeetCode 104: Maximum Depth of Binary Tree (Easy)
Time: O(n), Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    sol = Solution()
    # 3 -> 9, (20 -> 15, 7)
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("Test 1 Depth:", sol.maxDepth(tree))  # 3
