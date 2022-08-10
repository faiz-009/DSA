def countAndSay(n):
    if n==1:
        return '1'
    
    s = countAndSay(n-1)
    
    i=0
    j=0
    count=0
    st = ''
    n=len(s)
    while i<n :
        if s[i] == s[j]:
            count += 1
            i+= 1
        else:
                st += str(count) + s[j]
                count = 0
                j = i
    st += str(count) + s[j]
    return st

if __name__ == '__main__':
    #code
    n = int(input("Enter n: "))
    print(countAndSay(n))
    
        