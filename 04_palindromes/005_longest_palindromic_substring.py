"""
LeetCode 5: Longest Palindromic Substring (Medium)
Time: O(n^2), Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            res = max(res, p1, p2, key=len)

        return res


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (babad):", s.longestPalindrome("babad"))  # "bab" or "aba"
    print("Test 2 (cbbd):", s.longestPalindrome("cbbd"))    # "bb"
    print("Test 3 (a):", s.longestPalindrome("a"))          # "a"
