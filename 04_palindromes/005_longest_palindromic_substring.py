"""
LeetCode 5: Longest Palindromic Substring (Medium)
Патерн: Expand Around Center (Розширення від центру)
Час: O(n^2), Пам'ять: O(1)
Чому не Sliding Window: Паліндром не має монотонності — він дзеркальний відносно центру!
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(left: int, right: int) -> str:
            # Розсуваємо руки в боки, поки літери однакові
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Повертаємо паліндром (left+1 бо зробили зайвий крок вліво, right не включно)
            return s[left + 1 : right]

        for i in range(len(s)):
            # Непарний паліндром (центр — 1 буква, як "aba")
            p1 = expand(i, i)
            # Парний паліндром (центр — 2 букви, як "abba")
            p2 = expand(i, i + 1)

            # Оновлюємо найдовший
            res = max(res, p1, p2, key=len)

        return res


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (babad):", s.longestPalindrome("babad"))  # "bab" або "aba"
    print("Test 2 (cbbd):", s.longestPalindrome("cbbd"))    # "bb"
    print("Test 3 (a):", s.longestPalindrome("a"))          # "a"
