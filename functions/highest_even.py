# def highest_even(li: list[int]) -> int:
#     highest = None
#     for num in li:
#         if (highest == None or num > highest) and num % 2 == 0:
#             highest = num
#     return highest


# print(highest_even([1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]))


def highest_even(li: list[int]) -> int:
    return max((num for num in li if num % 2 == 0), default=None)


# defau lt is important because if there are no even numbers, max will raise a ValueError.
# By setting default to None, we can handle that case gracefully.


def calculate_sum(li: list[int]) -> int:
    return sum(num for num in li if num % 2 == 0)


print(highest_even([1, 3, 5, 11, 13, 15]))
print(calculate_sum([1, 3, 5, 11, 13, 15]))
