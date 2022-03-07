def binarySearch(arr,target):

    i = 0
    j = len(arr) - 1

    while i <= j:

        mid = i + (j - i)//2

        if arr[mid] == target:
            return True
        
        if arr[mid] < target:
            i = mid + 1

        else:
            j = mid -1
        
    return False

def searchInMatrix(arr, target):

    i = 0
    j = len(arr) - 1

    while i <= j:

        mid = i + (j - i)//2

        if target >= arr[mid][0] and target <= arr[mid][len(arr)-1]:

            return binarySearch(arr[mid],target)
        
        if target < arr[mid][0]:
            j = mid - 1

        else:
            i = mid + 1
    
    return False

matrix = [[1,3,5,7], [10,11,15,17],[22,29,32,45]]
target = 3

print(searchInMatrix(matrix,target))

