"""
LeetCode 347: Top K Frequent Elements (Medium)
Time: O(n log k), Space: O(n)
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print("Test 2:", sol.topKFrequent([1], 1))                  # [1]
