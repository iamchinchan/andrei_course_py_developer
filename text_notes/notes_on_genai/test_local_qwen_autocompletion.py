# now lets define a factorial function and test it
def fact(n):

    if type(n) != int or n < 0:
        return "Error: input must be an positive integer"
    elif n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))

# lets write more edge case tests using prints here
print(fact(0))
print(fact(1))
print(fact(-3))
print(fact(2.4))
print(fact("a"))
print(fact([1, 2]))
print(fact({}))
print(fact((1, 2)))
print(fact(True))
print(fact(False))
print(fact(None))


# lets have a fibonacci function
def fibonacci(n):
    if type(n) != int or n < 0:
        return "Error: input must be an positive integer"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

# lets write more edge case tests using prints here
print(fibonacci(-3))
print(fibonacci("a"))
print(fibonacci([1, 2]))
print(fibonacci({}))
print(fibonacci((1, 2)))
print(fibonacci(True))
print(fibonacci(False))
print(fibonacci(None))


# now i think autocompletion is working fine with my local model yipee


# lets write function to check if prime or not
def is_prime(n):
    """check if a number is prime or not"""
    if type(n) != int or n < 0:
        return "Error: input must be an positive integer"
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


print(is_prime(-3))
print(is_prime("a"))
print(is_prime([1, 2]))
print(is_prime({}))
print(is_prime((1, 2)))
print(is_prime(True))
print(is_prime(False))
print(is_prime(None))
print(is_prime(0))
print(is_prime(1))
print(is_prime(2.4))


# lets write a code for factorial using recursion
def factorial(n):
    if type(n) != int or n < 0:
        return "Error: input must be an positive integer"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
