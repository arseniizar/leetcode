"""
LeetCode 525: Contiguous Array (Medium)
Time: O(n), Space: O(n)
"""

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        seen = {0: -1}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1

            if current_sum in seen:
                max_len = max(max_len, i - seen[current_sum])
            else:
                seen[current_sum] = i

        return max_len


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.findMaxLength([0, 1]))                    # 2
    print("Test 2:", s.findMaxLength([0, 1, 0]))                 # 2
    print("Test 3:", s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0])) # 6
