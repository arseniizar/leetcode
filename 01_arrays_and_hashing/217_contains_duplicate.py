"""
LeetCode 217: Contains Duplicate (Easy)
Патерн: Hash Set
Час: O(n), Пам'ять: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Порівнюємо довжину списку та множини унікальних елементів
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.containsDuplicate([1, 2, 3, 1]))  # True
    print("Test 2:", s.containsDuplicate([1, 2, 3, 4]))  # False
