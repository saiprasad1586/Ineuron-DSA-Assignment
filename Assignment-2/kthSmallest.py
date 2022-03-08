def partition(arr,p,q):
    pivot = arr[p]
    i = p + 1
    j = q

    while i <= j:
        while i < len(arr) and arr[i] <= pivot:
            i += 1

        while arr[j] >pivot:
            j -= 1
        
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[j],arr[p] = arr[p],arr[j]

    return j

def findKthsmallest(arr, i,j,target):
    if i <= j:

        p = partition(arr, i, j)

        if p == target - 1:
            return arr[p]
        
        if p > k - 1:
            return findKthsmallest(arr,i,p, target)
        else:
            return findKthsmallest(arr,p + 1, j, target)
    return -1



A = [10, 3, 7, 13, 23, 15, 46, 24]
k = 4


x = findKthsmallest(A,0,len(A) - 1,k)
print(x)
