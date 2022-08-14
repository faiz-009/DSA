#print maximum sum subarray
import sys

a = [1,2,-3,4,-5,0,6,-2]
n = len(a)
max = -sys.maxsize
sum = 0
for i in range(n):
    sum = sum+a[i]
    if sum>max:
        max = sum
    if sum<0:
        sum=0
print(max)