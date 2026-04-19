class Solution:
    def search(self, arr, x):
        
        for num in range(len(arr)):
            if arr[num]==x:
                return num
        return -1