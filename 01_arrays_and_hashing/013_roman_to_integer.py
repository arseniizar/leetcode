"""
LeetCode 13: Roman to Integer (Easy)
Pattern: Hash Map + Subtractive Invariant
Time: O(n), Space: O(1)
Rule: If the current numeral is smaller than the next numeral, subtract it; otherwise, add it.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0

        for i in range(len(s)):
            # If current numeral is smaller than the next -> subtract
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (III):", s.romanToInt("III"))          # 3
    print("Test 2 (LVIII):", s.romanToInt("LVIII"))      # 58
    print("Test 3 (MCMXCIV):", s.romanToInt("MCMXCIV"))  # 1994
