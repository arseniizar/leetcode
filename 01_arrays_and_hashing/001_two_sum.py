"""
LeetCode 1: Two Sum (Easy)
Патерн: Hash Map (Словник за 1 прохід)
Час: O(n), Пам'ять: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # {значення: індекс}

        for i, num in enumerate(nums):
            diff = target - num
            # Якщо друге число вже траплялося в минулому
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print("Test 2:", s.twoSum([3, 2, 4], 6))        # [1, 2]
    print("Test 3:", s.twoSum([3, 3], 6))           # [0, 1]
