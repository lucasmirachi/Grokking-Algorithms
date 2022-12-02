def binarySearch(list, item):
    low = 0 # First item of list
    high = len(list) - 1 # Last item of list

    while low <= high:
        mid = (low + high) // 2 # // will round the division down in order to result in an integer
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

list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Change these values for testing
item = 8 #Can also change this value for testing

guess = binarySearch(list, item)
print("The chosen item was ", item, "and the algorithm guessed ", guess)