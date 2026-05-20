class Solution:
	def twoSum(self, arr, target):
		
		# initialize the empty dictionary
		seen = {}
		
		# for loop using enumerate
		for index, num in enumerate(arr):
		    # core logic of complete
		    complement = target - num
		    
		    # if complement in seen
		    if complement in seen:
		        # return the complement index and current position index
		        return [seen[complement], index]
		        
		    # if complement not in seen, then add the num and index
		    # for further lookum
		    seen[num] = index