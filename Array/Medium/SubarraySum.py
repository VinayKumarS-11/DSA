from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = {0: 1}
        presum = 0
        count = 0

        for i in range(n):
            presum += nums[i]
            remove = presum - k

            if remove in mp:
                count += mp[remove]

            mp[presum] = mp.get(presum, 0) + 1

        return count


obj = Solution()
nums = [1, 1, 1]
k = 2
result = obj.subarraySum(nums, k)

print("Subarray Sum:",result)
