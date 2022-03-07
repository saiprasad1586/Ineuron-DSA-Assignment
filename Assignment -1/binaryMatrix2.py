def SearchMatrix(arr,target):

    i = 0
    j = len(arr[0]) - 1

    while i < len(arr) and j >= 0:

        if arr[i][j] == target:
            return True

        if arr[i][j] >target:
            j -= 1

        else:
            i += 1

    return False

matrix=[[1,4,7,11,15], [2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,28,30]]
target=5

print(SearchMatrix(matrix,target))