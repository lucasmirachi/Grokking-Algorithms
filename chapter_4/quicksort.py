def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lowers = [i for i in arr[1:] if i<= pivot] #Subarray of all values lower than pivot
        highers = [i for i in arr[1:] if i> pivot] #Subarray of all values higher than pivot
        return quicksort(lowers) + [pivot] + quicksort(highers)

print(quicksort([10, 5, 3, 2])) 