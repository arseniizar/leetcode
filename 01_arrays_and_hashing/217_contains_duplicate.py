"""
LeetCode 217: Contains Duplicate (Easy)
Time: O(n), Space: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.containsDuplicate([1, 2, 3, 1]))  # True
    print("Test 2:", s.containsDuplicate([1, 2, 3, 4]))  # False
