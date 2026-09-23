"""
LeetCode 3: Longest Substring Without Repeating Characters (Medium)
Патерн: Sliding Window (Ковзне вікно з сетом)
Час: O(n), Пам'ять: O(min(n, m))
Ідея:
  - right розширює вікно
  - якщо зустріли дублікат — стискаємо вікно зліва (left += 1), поки дублікат не випаде
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Якщо буква вже є у вікні — підтягуємо лівий край
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
    print("Test 4 (пусто):", s.lengthOfLongestSubstring(""))             # 0
