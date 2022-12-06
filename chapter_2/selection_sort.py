def searchLower(arr):
    lower = arr[0] #store the lower value
    lower_index = 0 #store the lower value's index inside the array

    for i in range(1, len(arr)):
        if arr[i] < lower:
            lower = arr[i]
            lower_index = i
    return lower_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        lower = searchLower(arr)
        newArr.append(arr.pop(lower))
    return newArr

testArr = [5, 3, 6, 2, 10]
print("The test array is", testArr)
print("The sorted array is", selectionSort(testArr))