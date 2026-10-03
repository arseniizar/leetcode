"""
LeetCode 153: Find Minimum in Rotated Sorted Array (Medium)
Time: O(log n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return nums[l];
    }
};
```
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 ([3,4,5,1,2]):", sol.findMin([3, 4, 5, 1, 2]))           # 1
    print("Test 2 ([4,5,6,7,0,1,2]):", sol.findMin([4, 5, 6, 7, 0, 1, 2])) # 0
    print("Test 3 ([11,13,15,17]):", sol.findMin([11, 13, 15, 17]))       # 11
