"""
LeetCode 125: Valid Palindrome (Easy)
Патерн: Two Pointers (Зустрічні вказівники)
Час: O(n), Пам'ять: O(1)
Ідея: Два пальці рухаються назустріч, ігноруючи небуквенні символи та регістр.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Пропускаємо все, що не є літерою або цифрою
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print("Test 2:", sol.isPalindrome("race a car"))                      # False
    print("Test 3:", sol.isPalindrome(" "))                               # True
