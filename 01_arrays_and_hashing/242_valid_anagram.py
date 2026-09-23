"""
LeetCode 242: Valid Anagram (Easy)
Патерн: Hash Map / Frequency Counter
Час: O(n), Пам'ять: O(1) (бо літер в алфавіті максимум 26)
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isAnagram("anagram", "nagaram"))  # True
    print("Test 2:", sol.isAnagram("rat", "car"))          # False
