# This is a simple code to visualize and test the recursion of a function.
# Basically, a recursion is the technique of making a function call itself (in this case, the factorial() function) 
# This technique provides a way to break complicated problems down into simple problems which are easier to solve.

def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i-1)

print(factorial(6))