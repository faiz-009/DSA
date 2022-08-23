
def rotateByOne(b,n):
    key = b[0]
    for i in range(1,n):
        b[i-1]= b[i]
    b[n-1] = key
    return b

def fun(s1, s2, n):

    a = list(s1)
    b = list(s2)
    for i in range(n):
        if a == b :
            return True
        else:
            b = rotateByOne(b,n)
            if b == a:
                return True

    return False

if __name__ == '__main__':
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")

    n = len(s1)
    print(fun(s1,s2,n))



