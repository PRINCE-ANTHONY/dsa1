class Solution:
    def largest(self, arr):
        largest = arr[0]   # assume first element is largest
    
        for num in arr:
            if num > largest:
                largest = num
    
        return largest