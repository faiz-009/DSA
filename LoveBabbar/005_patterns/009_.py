'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

'''

n = int(input("Enter size: "))

for i in range(n):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(1, 2*i+2):
        print("*",end = '')
    print()
    
for i in range(n):
    for k in range(i):
        print(" ",end='')
    for j in range(1, 2*n - 2*i ):
        print("*",end = '')
    print()