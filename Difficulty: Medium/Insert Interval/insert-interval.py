class Solution:
    def insertInterval(self, intervals, newInterval):
        
        n = len(intervals)
        result = []
        i = 0
        
        # add intervals coming before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # add overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        result.append(newInterval)
        
        # all intervals after the overlapping intervals
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result
            
            
            
        