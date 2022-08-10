'''Given strings str1 and str2. The task is to find if str1 is a substring in the shuffled form of str2 or not. Print “YES” if str1 is a substring in shuffled form of str2 else print “NO”. 

Example 

Input: str1 = “onetwofour”, str2 = “hellofourtwooneworld” 
Output: YES 
Explanation: str1 is substring in shuffled form of str2 as 
str2 = “hello” + “fourtwoone” + “world” 
str2 = “hello” + str1 + “world”, where str1 = “fourtwoone” (shuffled form) 
Hence, str1 is a substring of str2 in shuffled form.

Input: str1 = “roseyellow”, str2 = “yellow” 
Output: NO 
Explanation: As the length of str1 is greater than str2. Hence, str1 is not a substring of str2.'''


def validShuffle(a,b):
    n = len(a)
    m = len(b)
    
    if n>m: return False

    a = sorted(a)

    for i in range(m):
        s = b[i:i+4]
        s = sorted(s)
        if s == a:
            return True
    
    return False
        

if __name__ == '__main__':
    #code
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")

    print(validShuffle(str1, str2))

