class Solution:
	def countOddEven(self, arr):
	    o=0
	    e=0
	    for nums in arr:
	        if nums%2==0:
	            e+=1
            else:
                o+=1
        return o,e