"""
LeetCode 3: Longest Substring Without Repeating Characters (Medium)
Time: O(n), Space: O(min(n, m))

C++ Solution:
```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> char_set;
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < s.size(); ++right) {
            while (char_set.count(s[right])) {
                char_set.erase(s[left]);
                ++left;
            }
            char_set.insert(s[right]);
            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};
```
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    s = Solution()
    print("Test 1 (abcabcbb):", s.lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
    print("Test 2 (bbbbb):", s.lengthOfLongestSubstring("bbbbb"))        # 1 ("b")
    print("Test 3 (pwwkew):", s.lengthOfLongestSubstring("pwwkew"))      # 3 ("wke")
    print("Test 4 (empty):", s.lengthOfLongestSubstring(""))             # 0
