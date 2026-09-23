"""
LeetCode 26: Remove Duplicates from Sorted Array (Easy)
Патерн: Two Pointers (Швидкий і повільний вказівник)
Час: O(n), Пам'ять: O(1)
Ідея: Замість видалення зсуваємо унікальні елементи на початок масиву.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # k — індекс, куди записуємо наступне унікальне число
        k = 1

        for i in range(1, len(nums)):
            # Якщо число відрізняється від попереднього — воно унікальне!
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 1, 2]
    k1 = s.removeDuplicates(arr1)
    print("Test 1: k =", k1, "nums =", arr1[:k1])  # k = 2, nums = [1, 2]

    arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = s.removeDuplicates(arr2)
    print("Test 2: k =", k2, "nums =", arr2[:k2])  # k = 5, nums = [0, 1, 2, 3, 4]
