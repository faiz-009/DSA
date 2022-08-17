'''
Permutations of a given string
Medium  

Given a string S. The task is to print all unique permutations of the given string in lexicographically sorted order.

 

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .
Example 2:

Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.
'''

def permute(s,n, ans):
    if n==1:
        ans += s
        print(ans)
        return 
    for i in range(n):
        s2 = ''
        for j in range(n):
            if s[j] != s[i]:
                s2 += s[j]
        permute(s2, n-1, ans+s[i])

if __name__ == '__main__':
    #code
    s = input("Enter the string : ")
    n = len(s)
    print("Permutations of the string are: ")
    permute(s,n, '')