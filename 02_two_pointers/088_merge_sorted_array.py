"""
LeetCode 88: Merge Sorted Array (Easy)
Time: O(m + n), Space: O(1)
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [2, 5, 6], 3)
    print("Test 1:", nums1)  # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    s.merge(nums1, 1, [], 0)
    print("Test 2:", nums1)  # [1]

    nums1 = [0]
    s.merge(nums1, 0, [1], 1)
    print("Test 3:", nums1)  # [1]
