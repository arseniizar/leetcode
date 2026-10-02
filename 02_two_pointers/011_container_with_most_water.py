"""
LeetCode 11: Container With Most Water (Medium)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int ma = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            int hl = heights[l];
            int hr = heights[r];
            int h = min(hl, hr);
            ma = max(ma, h * (r - l));

            if (hl < hr) ++l;
            else --r;
        }

        return ma;
    }
};
```
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            h = min(heights[l], heights[r])
            max_area = max(max_area, h * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print("Test 2:", sol.maxArea([1, 1]))                        # 1
    print("Test 3:", sol.maxArea([4, 3, 2, 1, 4]))               # 16
