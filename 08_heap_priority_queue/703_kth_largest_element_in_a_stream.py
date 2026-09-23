"""
LeetCode 703: Kth Largest Element in a Stream (Easy)
Pattern: Min-Heap of Size K
Time: O(n log k), Space: O(k)
Idea: Maintain a heap of exactly k largest elements. The smallest of them (at the root) is the kth largest!
"""
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # Evict smaller elements until the heap size is exactly k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # 4
    print(kth.add(5))   # 5
    print(kth.add(10))  # 5
    print(kth.add(9))   # 8
    print(kth.add(4))   # 8
