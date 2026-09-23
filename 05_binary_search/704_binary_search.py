"""
LeetCode 704: Binary Search (Easy)
Time: O(log n), Space: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print("Test 2:", sol.search([-1, 0, 3, 5, 9, 12], 2))  # -1
