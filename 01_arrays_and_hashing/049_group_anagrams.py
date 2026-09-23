"""
LeetCode 49: Group Anagrams (Medium)
Патерн: Hash Map with Sorted String or Frequency Tuple Key
Час: O(n * k log k), Пам'ять: O(n * k)
Ідея: Усі анаграми після сортування букв виглядають абсолютно однаково!
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Ключем є відсортований рядок
            sorted_key = "".join(sorted(s))
            groups[sorted_key].append(s)

        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("Test 2:", sol.groupAnagrams([""]))
    print("Test 3:", sol.groupAnagrams(["a"]))
