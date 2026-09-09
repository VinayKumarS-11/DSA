class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        intervals.sort()
        for intervals in intervals:
            if not ans or ans[-1][1] < intervals[0]:
                  ans.append(intervals)
            else:
                ans[-1][1]=max(ans[-1][1], intervals[1])      


        return ans


sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(intervals))    
        