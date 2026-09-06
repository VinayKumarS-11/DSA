from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        el1 = None
        el2 = None
        ct1 = 0
        ct2 = 0

        # First pass: find two possible candidates
        for i in range(n):

            if ct1 == 0 and nums[i] != el2:
                ct1 = 1
                el1 = nums[i]

            elif ct2 == 0 and nums[i] != el1:
                ct2 = 1
                el2 = nums[i]

            elif nums[i] == el1:
                ct1 += 1

            elif nums[i] == el2:
                ct2 += 1

            else:
                ct1 -= 1
                ct2 -= 1

        # Second pass: verify candidates
        ct1 = 0
        ct2 = 0

        for num in nums:
            if num == el1:
                ct1 += 1
            elif num == el2:
                ct2 += 1

        # Find elements appearing more than n/3 times
        result = []
        mini = n // 3

        if ct1 > mini:
            result.append(el1)

        if ct2 > mini:
            result.append(el2)

        return result


# Input
nums = [2, 1, 1, 3, 1, 4, 5, 6]

obj = Solution()

answer = obj.majorityElement(nums)


print("Input:", nums)
print("Output:", answer)

