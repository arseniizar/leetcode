"""
LeetCode 525: Contiguous Array (Medium)
Pattern: Prefix Sum + Hash Map (0 -> -1 transformation)
Time: O(n), Space: O(n)
Idea: Map 0 to -1. Equal counts of 0 and 1 mean sum = 0.
      If the current prefix sum was seen before, the subarray between the two occurrences has sum 0!
"""

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        seen = {0: -1}  # {prefix_sum: earliest_index}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            # 1 -> +1, 0 -> -1
            current_sum += 1 if num == 1 else -1

            if current_sum in seen:
                max_len = max(max_len, i - seen[current_sum])
            else:
                # Store ONLY the earliest index to maximize window length
                seen[current_sum] = i

        return max_len


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.findMaxLength([0, 1]))                    # 2
    print("Test 2:", s.findMaxLength([0, 1, 0]))                 # 2
    print("Test 3:", s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0])) # 6
