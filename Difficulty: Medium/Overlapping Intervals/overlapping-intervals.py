class Solution:
    def mergeOverlap(self, arr):
        # Sort the intervals chronologically based on start times
        arr.sort(key = lambda x: x[0])
        
        # Initialize an empty list to store merged intervals
        merged = []
        
        for i in arr:
            # If merged is empty or no overlap exists, append current interval
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            # If an overlap exists, update the end time of the last merged interval
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
                
        return merged