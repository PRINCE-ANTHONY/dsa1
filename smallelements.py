class Solution:
    def countOfElements(self, x, arr):
        l=0
        # Code Here
        for nums in arr:
            if nums<=x:
                l+=1
            
        return l