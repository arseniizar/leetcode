"""
LeetCode 121: Best Time to Buy and Sell Stock (Easy)
Патерн: One-Pass / Tracking Minimum (Greedy / Sliding Window)
Час: O(n), Пам'ять: O(1)
Ідея: Тримаємо мінімальну ціну з минулого і порівнюємо з поточним днем.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5 (купити за 1, продати за 6)
    print("Test 2:", s.maxProfit([7, 6, 4, 3, 1]))     # 0 (ціни тільки падають)
