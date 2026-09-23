"""
LeetCode 4: Median of Two Sorted Arrays (Hard)
Патерн: Binary Search on Partitions
Час: O(log(min(m, n))), Пам'ять: O(1)
Ідея: Робимо бінарний пошук по меншому масиву, шукаючи такий розріз (partition),
      щоб ліва половина об'єднаного масиву містила рівно половину елементів і всі її числа
      були менші або рівні за числа правої половини.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        # Завжди робимо бінарний пошук по меншому масиву
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # індекс розрізу в A
            j = half - i - 2  # індекс розрізу в B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Правильний розріз знайдено
            if Aleft <= Bright and Bleft <= Aright:
                # Якщо загальна кількість елементів непарна
                if total % 2 != 0:
                    return float(min(Aright, Bright))
                # Якщо парна
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.findMedianSortedArrays([1, 3], [2]))        # 2.0
    print("Test 2:", sol.findMedianSortedArrays([1, 2], [3, 4]))     # 2.5
