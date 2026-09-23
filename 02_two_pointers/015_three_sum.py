"""
LeetCode 15: 3Sum (Medium)
Pattern: Sorting + Converging Two Pointers
Time: O(n^2), Space: O(1) extra space (or O(n) for sorting/output)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print("Test 2:", s.threeSum([0, 1, 1]))               # []
    print("Test 3:", s.threeSum([0, 0, 0]))               # [[0, 0, 0]]
