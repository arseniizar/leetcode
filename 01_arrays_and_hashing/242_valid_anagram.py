"""
LeetCode 242: Valid Anagram (Easy)
Time: O(n), Space: O(1)
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isAnagram("anagram", "nagaram"))  # True
    print("Test 2:", sol.isAnagram("rat", "car"))          # False
