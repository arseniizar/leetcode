"""
LeetCode 525: Contiguous Array (Medium)
Патерн: Prefix Sum + Hash Map (0 -> -1)
Час: O(n), Пам'ять: O(n)
Ідея: Замінюємо 0 на -1. Рівна кількість 0 і 1 означає суму 0.
      Якщо поточна сума вже зустрічалася раніше, відрізок між ними має суму 0!
"""

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        seen = {0: -1}  # {сума: найперший_індекс}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            # 1 -> +1, 0 -> -1
            current_sum += 1 if num == 1 else -1

            if current_sum in seen:
                max_len = max(max_len, i - seen[current_sum])
            else:
                # Зберігаємо ТІЛЬКИ перший індекс для максимальної довжини
                seen[current_sum] = i

        return max_len


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.findMaxLength([0, 1]))                    # 2
    print("Test 2:", s.findMaxLength([0, 1, 0]))                 # 2
    print("Test 3:", s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0])) # 6
