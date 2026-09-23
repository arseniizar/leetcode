"""
LeetCode 20: Valid Parentheses (Easy)
Патерн: Stack (Стек - LIFO)
Час: O(n), Пам'ять: O(n)
Ідея: Відкриваючу дужку кладемо в стек. Для закриваючої — дістаємо останню зі стеку і порівнюємо.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching:
                # Якщо стек не порожній і верхній елемент збігається
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
