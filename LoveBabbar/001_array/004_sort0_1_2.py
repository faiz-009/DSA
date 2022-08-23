'''
Sort an array of 0s, 1s and 2s
Easy 

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
*** without using extra space ***

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.
'''

from msilib.schema import BBControl


def swap(arr, a,b):
    temp = a
    a = b
    b= temp
    return arr

if __name__ == '__main__':
    #code
    a = [2,1,0,2,1,0,0,2,1,1,1,2,2,2,0,0,1,2]
    n = len(a)
    
    low = 0
    mid = 0
    high = n-1
    print(a)
    
    while mid<= high:
        if a[mid] == 0:
            a = swap(a, a[mid], a[low])
            mid +=1
            low +=1
        elif a[mid] == 1:
            mid += 1
        else:
            a= swap(a, a[mid], a[high])
            high -=1
    print(a)