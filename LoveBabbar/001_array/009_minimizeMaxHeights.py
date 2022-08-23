#User function Template for python

def getMinDiff(arr, n, k):
        # code here
        arr.sort()
        high = arr[n-1]
        low = arr[0]
        diff = high - low
        
        for i in range(1, n):
            
            if arr[i]<k : continue
        
            low = min(arr[0]+k, arr[i]-k)
            
            high = max(arr[i-1]+k, arr[n-1]-k)
            
            diff = min(diff, high - low)
        return diff

arr = [1, 15, 10]
n = len(arr)
k = 6
print(getMinDiff(arr, n, k))