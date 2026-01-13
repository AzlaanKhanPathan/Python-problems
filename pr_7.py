# Write a program to calculate the factorial of a number using a loop.

def factorial(n):
    ans = 1 # the first number
    i = 1 # keeping the index 1 
    while (i <= n):  # loop through 1 to nth number 
        ans *= i # incrementing the value 
        i += 1 # #incrementing the index as well 
    return ans  
        
print(factorial(5))
