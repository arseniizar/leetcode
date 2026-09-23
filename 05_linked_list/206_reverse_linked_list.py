"""
LeetCode 206: Reverse Linked List (Easy)
Time: O(n), Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def to_list(node: ListNode | None) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


def to_linked_list(lst: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    ll = to_linked_list([1, 2, 3, 4, 5])
    print("Test 1:", to_list(sol.reverseList(ll)))  # [5, 4, 3, 2, 1]
