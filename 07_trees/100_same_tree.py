"""
LeetCode 100: Same Tree (Easy)
Pattern: Tree / DFS (Recursive Node Comparison)
Time: O(n), Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both empty
        if not p and not q:
            return True
        # One is empty, or values don't match
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Test 1 (Identical):", sol.isSameTree(t1, t2))  # True

    t3 = TreeNode(1, TreeNode(2))
    t4 = TreeNode(1, None, TreeNode(2))
    print("Test 2 (Different):", sol.isSameTree(t3, t4))  # False
