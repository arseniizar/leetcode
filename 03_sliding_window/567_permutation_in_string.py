"""
LeetCode 567: Permutation in String (Medium)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size(), n2 = s2.size();
        if (n2 < n1) return false;

        vector<int> c(26, 0);
        for (char ch : s1) c[ch - 'a']++;

        int f = n1;

        for (int r = 0; r < n2; ++r) {
            if (c[s2[r] - 'a'] > 0) f--;
            c[s2[r] - 'a']--;

            if (r >= n1) {
                if (c[s2[r - n1] - 'a'] >= 0) f++;
                c[s2[r - n1] - 'a']++;
            }

            if (f == 0) return true;
        }

        return false;
    }
};
```
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        c = [0] * 26
        for ch in s1:
            c[ord(ch) - ord('a')] += 1

        f = n1

        for r in range(n2):
            if c[ord(s2[r]) - ord('a')] > 0:
                f -= 1
            c[ord(s2[r]) - ord('a')] -= 1

            if r >= n1:
                if c[ord(s2[r - n1]) - ord('a')] >= 0:
                    f += 1
                c[ord(s2[r - n1]) - ord('a')] += 1

            if f == 0:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 (s1=ab, s2=eidbaooo):", sol.checkInclusion("ab", "eidbaooo"))  # True
    print("Test 2 (s1=ab, s2=eidboaoo):", sol.checkInclusion("ab", "eidboaoo"))  # False
