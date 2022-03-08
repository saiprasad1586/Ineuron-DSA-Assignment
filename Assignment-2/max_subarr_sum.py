import re
import sys


def max_sum(arr, p ,mid, q):
    
    max1 = -sys.maxsize
    sum1 = 0

    for i in range(mid, p - 1, -1):
        # print(i)
        sum1 += arr[i]

        if sum1 > max1:
            max1 = sum1

    max2 = -sys.maxsize
    sum1 = 0

    for i in range(mid + 1,q + 1):
        sum1 += arr[i]

        if sum1 > max2:
            max2 = sum1

    # maxf = max(max_subarr_sum(arr, p, mid), max_subarr_sum(arr, mid + 1, q))

    return max(max1, max2, max1 + max2)

def max_sub_array_sum(arr,i,j):

    if i == j:
        return arr[i]

    mid = i + (j - i)//2

    return max(max_sub_array_sum(arr, i , mid), max_sub_array_sum(arr, mid + 1, j), max_sum(arr, i, mid, j))    





A=[-5,-10,6,3,-1,-2,13,4,-9,-1,4,12,-3,0]

# print(len(A))

print(max_sub_array_sum(A, 0, len(A) - 1))