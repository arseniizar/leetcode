"""
LeetCode 1046: Last Stone Weight (Easy)
Патерн: Max-Heap (Купа / Пріоритетна черга через heapq з мінусом)
Час: O(n log n), Пам'ять: O(n)
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # У Python heapq реалізує Min-Heap, тому множимо на -1 для Max-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 1
    print("Test 2:", sol.lastStoneWeight([1]))                  # 1
