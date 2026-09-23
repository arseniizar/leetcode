"""
LeetCode 141: Linked List Cycle (Easy)
Pattern: Fast & Slow Pointers (Floyd's Tortoise and Hare)
Time: O(n), Space: O(1)
Idea: Slow pointer moves 1 step, fast pointer moves 2 steps. If a cycle exists, they must meet!
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    # Create list with cycle: 3 -> 2 -> 0 -> -4 -> 2...
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle

    print("Test 1 (with cycle):", sol.hasCycle(n1))  # True

    # List without cycle: 1 -> 2
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    print("Test 2 (no cycle):", sol.hasCycle(a))     # False
