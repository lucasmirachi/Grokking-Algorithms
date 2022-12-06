#Chapter4 - Exercise 1
#Write a code for the sum function where you must sum all the numbers of an array and return the total value using recursion

def sum(list):
    if list == []:
        return 0
    return list [0] + sum(list[1:])
    
list = [1,2,3,4,5]
print(sum(list))