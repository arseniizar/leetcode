"""
LeetCode 42: Trapping Rain Water (Hard)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int l = 0, r = n - 1;
        int lm = 0, rm = 0;
        int tw = 0;

        while (l < r) {
            int hl = height[l];
            int hr = height[r];
            if (hl < hr) {
                if (hl >= lm) {
                    lm = hl;
                } else {
                    tw += lm - hl;
                }
                ++l;
            } else {
                if (hr >= rm) {
                    rm = hr;
                } else {
                    tw += rm - hr;
                }
                --r;
            }
        }

        return tw;
    }
};
```
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        total_water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total_water += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total_water += right_max - height[r]
                r -= 1

        return total_water


if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print("Test 2:", sol.trap([4, 2, 0, 3, 2, 5]))                    # 9
    print("Test 3:", sol.trap([3, 0, 1, 0, 4]))                       # 8
