'''
Print all subsequences of a string

Difficulty Level : Medium
Last Updated : 18 Jul, 2022
Given a string, we have to find out all subsequences of it. A String is a subsequence of a given String, that is generated by deleting some character of a given string without changing its order.

Examples: 

Input : abc
Output : a, b, c, ab, bc, ac, abc

Input : aaa
Output : a, aa, aaa


'''
def subS(ans, i, n, s):
    if i==n:
        if ans=='':
            print("{}")
        else:
            print(ans)
    else:
        #exclude s[i]
        subS(ans, i+1, n, s)

        #include s[i]
        ans += s[i]
        subS(ans, i+1, n, s)
    return

if __name__ == '__main__':
    #code
    s = input("Enter the string : ")

    output = ''
    print("Subsequences of String are : ")
    subS(output, 0, len(s), s)