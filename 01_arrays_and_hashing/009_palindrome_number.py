"""
LeetCode 9: Palindrome Number (Easy)
Патерн: Math / Base-10 Reversal
Час: O(log10(n)), Пам'ять: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Від'ємні числа не можуть бути паліндромами
        if x < 0:
            return False

        t = x
        reversed_num = 0

        # Збираємо число задом наперед через * 10 + остання_цифра
        while t > 0:
            last_digit = t % 10
            reversed_num = reversed_num * 10 + last_digit
            t //= 10

        return reversed_num == x


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (121):", s.isPalindrome(121))    # True
    print("Test 2 (-121):", s.isPalindrome(-121))  # False
    print("Test 3 (10):", s.isPalindrome(10))      # False
    print("Test 4 (1001):", s.isPalindrome(1001))  # True
