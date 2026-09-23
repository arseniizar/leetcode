"""
LeetCode 13: Roman to Integer (Easy)
Патерн: Hash Map + Subtractive Invariant
Час: O(n), Пам'ять: O(1)
Правило: якщо поточна літера менша за наступну — віднімаємо, інакше — додаємо.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0

        for i in range(len(s)):
            # Якщо поточна менша за наступну -> віднімаємо
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
