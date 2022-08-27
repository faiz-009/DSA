'''
*********
 *******
  *****
   ***
    *

'''
n = int(input("Enter size: "))

for i in range(1,n+1):
    for k in range(i):
        print(" ",end='')
    for j in range(2*n - 2*i + 1):
        print("*",end = '')
    print()