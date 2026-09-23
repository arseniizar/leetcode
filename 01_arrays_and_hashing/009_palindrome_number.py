"""
LeetCode 9: Palindrome Number (Easy)
Pattern: Math / Base-10 Digit Reversal
Time: O(log10(n)), Space: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        t = x
        reversed_num = 0

        # Construct reversed number: reversed_num * 10 + last_digit
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
