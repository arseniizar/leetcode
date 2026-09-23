"""
LeetCode 2: Add Two Numbers (Medium)
Pattern: Linked List + Dummy Head + Column Addition
Time: O(max(m, n)), Space: O(max(m, n))
Why reverse order: Least significant digits (units) come first, allowing straightforward left-to-right addition with carry!
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def to_linked_list(lst: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next


def to_list(node: ListNode | None) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


if __name__ == "__main__":
    s = Solution()
    # 342 + 465 = 807 -> [7, 0, 8]
    l1 = to_linked_list([2, 4, 3])
    l2 = to_linked_list([5, 6, 4])
    print("Test 1:", to_list(s.addTwoNumbers(l1, l2)))  # [7, 0, 8]

    # 0 + 0 = 0 -> [0]
    l1 = to_linked_list([0])
    l2 = to_linked_list([0])
    print("Test 2:", to_list(s.addTwoNumbers(l1, l2)))  # [0]

    # 9999999 + 9999 = 10009998 -> [8, 9, 9, 9, 0, 0, 0, 1]
    l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = to_linked_list([9, 9, 9, 9])
    print("Test 3:", to_list(s.addTwoNumbers(l1, l2)))  # [8, 9, 9, 9, 0, 0, 0, 1]
