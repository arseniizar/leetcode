"""
LeetCode 3: Longest Substring Without Repeating Characters (Medium)
Pattern: Sliding Window (Dynamic Window with Hash Set)
Time: O(n), Space: O(min(n, m))
Idea:
  - right pointer expands the window
  - when a duplicate is encountered, shrink the window from the left (left += 1) until valid
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If current character already exists in the window -> shrink left side
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
