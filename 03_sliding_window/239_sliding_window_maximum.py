"""
LeetCode 239: Sliding Window Maximum (Hard)
Time: O(n), Space: O(k)

C++ Solution:
```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> res;

        for (int i = 0; i < nums.size(); ++i) {
            // 1. Evict elements that fell outside the window from front
            if (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            // 2. Evict smaller elements from back
            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }

            // 3. Push current index to back
            dq.push_back(i);

            // 4. Record maximum once window reaches size k
            if (i >= k - 1) {
                res.push_back(nums[dq.front()]);
            }
        }

        return res;
    }
};
```
"""
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


if __name__ == "__main__":
    sol = Solution()
    print("Test 1 ([1,3,-1,-3,5,3,6,7], k=3):", sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)) # [3, 3, 5, 5, 6, 7]
    print("Test 2 ([1], k=1):", sol.maxSlidingWindow([1], 1))                                     # [1]
