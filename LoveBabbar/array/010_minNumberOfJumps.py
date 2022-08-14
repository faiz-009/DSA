#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    if n==1 : return 0
	    
	    if arr[0]==0: return -1
	    
	    step = arr[0]
	    maxReach = 0
	    count = 0
	    
	    for i in range(1,n):
	        step -=1
	        maxReach = max(maxReach, arr[i]-step)
	        
	        if step==0:
	            if maxReach <=0: return -1
	            count+=1
	            step = maxReach
	            maxReach = 0
	    if step>1 and step!=arr[n-1]:
	        return count+1
        
        return count
     


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends