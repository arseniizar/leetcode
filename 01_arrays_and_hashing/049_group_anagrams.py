"""
LeetCode 49: Group Anagrams (Medium)
Time: O(n * k log k), Space: O(n * k)
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))
            groups[sorted_key].append(s)

        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("Test 2:", sol.groupAnagrams([""]))
    print("Test 3:", sol.groupAnagrams(["a"]))
