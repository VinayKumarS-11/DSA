class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while left <= right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
    
nums = [1, 2, 4, 5, 8, 9]
target = 2

obj = Solution()
print(obj.search(nums, target))