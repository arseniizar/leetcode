"""
LeetCode 5: Longest Palindromic Substring (Medium)
Pattern: Expand Around Center
Time: O(n^2), Space: O(1)
Why not Sliding Window: Palindromes lack monotonicity; they are symmetric around their center.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(left: int, right: int) -> str:
            # Expand outward as long as characters match and indices are in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return valid palindrome slice (left+1 due to overstep, right is exclusive)
            return s[left + 1 : right]

        for i in range(len(s)):
            # Odd length palindrome (single character center, e.g., "aba")
            p1 = expand(i, i)
            # Even length palindrome (two character center, e.g., "abba")
            p2 = expand(i, i + 1)

            # Update the longest found palindrome
            res = max(res, p1, p2, key=len)

        return res


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (babad):", s.longestPalindrome("babad"))  # "bab" or "aba"
    print("Test 2 (cbbd):", s.longestPalindrome("cbbd"))    # "bb"
    print("Test 3 (a):", s.longestPalindrome("a"))          # "a"
