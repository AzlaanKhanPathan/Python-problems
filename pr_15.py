# Create a program to print the Fibonacci series up to N terms

n = 10
a, b = 0, 1 

for i in range(n):
    print(a, end=" ")

    a, b = b ,a + b
    