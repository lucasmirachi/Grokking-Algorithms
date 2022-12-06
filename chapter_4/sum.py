#Chapter4 - Exercise 1
#Write a code for the sum function where you must sum all the numbers of an array and return the total value using recursion

def sum(list):
    if list == []:
        return 0
    else:
        return sum(list[1:])
    
list = [1,2,3,4]
print(sum(list))