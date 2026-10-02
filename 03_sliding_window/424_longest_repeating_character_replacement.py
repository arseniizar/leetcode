"""
LeetCode 424: Longest Repeating Character Replacement (Medium)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26, 0);
        int max_freq = 0;
        int max_len = 0;
        int l = 0;

        for (int r = 0; r < s.size(); ++r) {
            count[s[r] - 'A']++;
            max_freq = max(max_freq, count[s[r] - 'A']);

            while ((r - l + 1) - max_freq > k) {
                count[s[l] - 'A']--;
                ++l;
            }

            max_len = max(max_len, r - l + 1);
        }

        return max_len;
    }
};
```
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_freq = 0
        max_len = 0
        l = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[r]) - ord('A')])

            while (r - l + 1) - max_freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 (XYYX, k=2):", sol.characterReplacement("XYYX", 2))      # 4
    print("Test 2 (AAABABB, k=1):", sol.characterReplacement("AAABABB", 1)) # 5
