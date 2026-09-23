"""
LeetCode 1: Two Sum (Easy)
Time: O(n), Space: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print("Test 2:", s.twoSum([3, 2, 4], 6))        # [1, 2]
    print("Test 3:", s.twoSum([3, 3], 6))           # [0, 1]
