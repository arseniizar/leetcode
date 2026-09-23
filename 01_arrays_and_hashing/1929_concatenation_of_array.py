"""
LeetCode 1929: Concatenation of Array (Easy)
Pattern: List Operations / Memory Allocation
Time: O(n), Space: O(n)
"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # Most idiomatic and fastest in Python:
        return nums + nums


# Manual pre-allocated buffer approach:
class SolutionManual:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.getConcatenation([1, 2, 1]))       # [1, 2, 1, 1, 2, 1]
    print("Test 2:", s.getConcatenation([1, 3, 2, 1]))    # [1, 3, 2, 1, 1, 3, 2, 1]
