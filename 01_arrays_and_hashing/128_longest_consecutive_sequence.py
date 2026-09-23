"""
LeetCode 128: Longest Consecutive Sequence (Medium)
Time: O(n), Space: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.longestConsecutive([100, 4, 200, 1, 3, 2]))               # 4
    print("Test 2:", s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))       # 9
    print("Test 3:", s.longestConsecutive([]))                                    # 0
