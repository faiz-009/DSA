'''Palindrome String
EasyAccuracy: 50.77%Submissions: 100k+Points: 2
Given a string S, check if it is palindrome or not.

Example 1:

Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome '''


#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		i=0
		j = len(S)-1
		while i<=j:
		    if S[i] != S[j]:
		        return 0
		    i+=1
		    j-=1
		return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends
