class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] <= end:
                if i[1] >= end:
                    end = i[1]
            else:
                ans.append([start, end])
                start = i[0]
                end = i[1]
        print(start, end)
        print(ans)
        ans.append([start, end])
        print(ans)
        return ans
