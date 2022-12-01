def binarySearch(list, item):
    low = 0 # First item of list
    high = len(list) - 1 # Last item of list

    while low <= high:
        mid = (low + high) // 2
        #print(mid)
        guess = list[mid]
        print(guess)
        if guess == item:
            return guess
        elif guess < item:
            low = mid + 1
        else :
            high = mid - 1
    return None

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 8

guess = binarySearch(list, item)
#print(guess)
