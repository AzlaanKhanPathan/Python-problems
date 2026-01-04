#Write a python program to check if num is even or odd
# def even_or_odd(arr):
#     return "Even" if arr % 2 == 0 else "Odd"

# print(even_or_odd(4))

# #Write a python program to check if sum of numbers is even or odd
def even_or_odd(arr):
    return "Even" if sum(arr) % 2 == 0 else "Odd"

print(even_or_odd([1,3,5,7,9]))

