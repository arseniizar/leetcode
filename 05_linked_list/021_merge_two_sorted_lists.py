"""
LeetCode 21: Merge Two Sorted Lists (Easy)
Патерн: Linked List + Dummy Head
Час: O(n + m), Пам'ять: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Приєднуємо хвіст, який залишився
        curr.next = list1 if list1 else list2

        return dummy.next


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
    l1 = to_linked_list([1, 2, 4])
    l2 = to_linked_list([1, 3, 4])
    print("Test 1:", to_list(sol.mergeTwoLists(l1, l2)))  # [1, 1, 2, 3, 4, 4]
