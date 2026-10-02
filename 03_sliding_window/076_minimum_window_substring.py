"""
LeetCode 76: Minimum Window Substring (Hard)
Time: O(n + m), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> c(128, 0);
        for (char ch : t) c[ch]++;

        int f = t.size();
        int min_len = INT_MAX;
        int start_idx = 0;
        int l = 0;

        for (int r = 0; r < s.size(); ++r) {
            if (c[s[r]] > 0) f--;
            c[s[r]]--;

            while (f == 0) {
                if (r - l + 1 < min_len) {
                    min_len = r - l + 1;
                    start_idx = l;
                }

                if (c[s[l]] >= 0) f++;
                c[s[l]]++;
                ++l;
            }
        }

        return min_len == INT_MAX ? "" : s.substr(start_idx, min_len);
    }
};
```
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = [0] * 128
        for ch in t:
            c[ord(ch)] += 1

        f = len(t)
        min_len = float("inf")
        start_idx = 0
        l = 0

        for r in range(len(s)):
            if c[ord(s[r])] > 0:
                f -= 1
            c[ord(s[r])] -= 1

            while f == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_idx = l

                if c[ord(s[l])] >= 0:
                    f += 1
                c[ord(s[l])] += 1
                l += 1

        return "" if min_len == float("inf") else s[start_idx : start_idx + min_len]


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 (s=ADOBECODEBANC, t=ABC):", sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
    print("Test 2 (s=a, t=a):", sol.minWindow("a", "a"))                            # "a"
    print("Test 3 (s=a, t=aa):", sol.minWindow("a", "aa"))                          # ""
