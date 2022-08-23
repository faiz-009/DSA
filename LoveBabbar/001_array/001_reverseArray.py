'''
Write a program to reverse an array or string

Difficulty Level : Basic
 
Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
'''

#list slicing
a = [1, 2, 5, 4, 3, 8]
print(a)
#b = a[::-1]
# print(b)

def swap(b, x, y):
    b[x] = b[x] + b[y]
    b[y] = b[x] - b[y]
    b[x] = b[x] - b[y]

#traditional method 
i = 0
j = len(a) -1
while i<j :

    swap(a, i, j)
    #a[i], a[j] = a[j], a[i]
    i+=1
    j-=1
print(a)

