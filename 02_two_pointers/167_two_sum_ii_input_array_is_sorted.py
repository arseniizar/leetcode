"""
LeetCode 167: Two Sum II - Input Array Is Sorted (Medium)
Time: O(n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) {
                return {l + 1, r + 1};
            } else if (sum < target) {
                ++l;
            } else {
                --r;
            }
        }

        return {};
    }
};
```
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        return []


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 ([2,7,11,15], target=9):", sol.twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print("Test 2 ([2,3,4], target=6):", sol.twoSum([2, 3, 4], 6))          # [1, 3]
    print("Test 3 ([-1,0], target=-1):", sol.twoSum([-1, 0], -1))          # [1, 2]
