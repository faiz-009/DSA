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
def isPalindrome(s):
    n = len(s)
    i = 0
    j = n-1
    while i <= j:
        if s[i] != s[j]:
            return False
        else:
            i+=1
            j-=1
    return True

def longestPalindrome(s,n, m):
    if m == 1  : 
        return s[0]
    if m == 2 :
        return s[:2]
    
    i = 0
    j = i+n
    while j<=m:
        a = s[i:j]
        if isPalindrome(a):
            return a
        else:
            i += 1 
            j += 1
    return longestPalindrome(s,n-1, m)



if __name__ == '__main__':
    #code
    s = input("Enter the string: ")
    n = len(s)
    m = len(s)

    print(longestPalindrome(s,n, m))
    #print(isPalindrome("aaba"))
