'''
Longest Palindrome in a String
Medium

Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).


Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.

'''
def longestPalindrome(s,n):
    size = n
    i=0
    j=size-1
    a = ''
    b = ''
    while i<=j:
        if s[i] == s[j]:
            a += s[i]
            if i !=j :
                b += s[j]
            i+=1
            j-=1
        else:
            return longestPalindrome(s,n-1)

if __name__ == '__main__':
    #code
    s = input("Enter the string: ")
    n = len(s)

    print(longestPalindrome(s,n))
