'''
    *
   ***
  *****
 *******
*********

'''
n = int(input("Enter size: "))

for i in range(n):
    for k in range(1, 2*i+1):
        print(" ",end='')
    for j in range(1, 2*i+2):
        print("*",end = '')
    print()