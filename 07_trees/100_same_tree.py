"""
LeetCode 100: Same Tree (Easy)
Патерн: Tree / DFS (Порівняння двох дерев)
Час: O(n), Пам'ять: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Якщо обидва порожні
        if not p and not q:
            return True
        # Якщо тільки одне з них порожнє, або значення не збігаються
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Test 1 (Однакові):", sol.isSameTree(t1, t2))  # True

    t3 = TreeNode(1, TreeNode(2))
    t4 = TreeNode(1, None, TreeNode(2))
    print("Test 2 (Різні):", sol.isSameTree(t3, t4))     # False
