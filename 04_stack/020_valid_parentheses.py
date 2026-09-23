"""
LeetCode 20: Valid Parentheses (Easy)
Time: O(n), Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching:
                top = stack.pop() if stack else '#'
                if matching[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 (()):", sol.isValid("()"))          # True
    print("Test 2 (()[{}]):", sol.isValid("()[]{}"))  # True
    print("Test 3 ((]):", sol.isValid("(]"))          # False
    print("Test 4 (([)]):", sol.isValid("([)]"))      # False
