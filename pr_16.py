# Write a program to find the GCD of two numbers.

def find_gcd(a,b):
    result = min(a,b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1 

    return result

print(find_gcd(10,28))
    