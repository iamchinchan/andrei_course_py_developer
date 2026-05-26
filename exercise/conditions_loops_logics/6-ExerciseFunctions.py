# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even(li):
    return max(x for x in li if x % 2 == 0)


print(highest_even([10, 2, 3, 4, 8, 11]))
