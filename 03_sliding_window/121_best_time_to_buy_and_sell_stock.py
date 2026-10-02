"""
LeetCode 121: Best Time to Buy and Sell Stock (Easy)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];
        int max_profit = 0;

        for (int price : prices) {
            min_price = min(min_price, price);
            max_profit = max(max_profit, price - min_price);
        }

        return max_profit;
    }
};
```
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
    print("Test 1:", s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5 (buy at 1, sell at 6)
    print("Test 2:", s.maxProfit([7, 6, 4, 3, 1]))     # 0 (prices only decrease)
