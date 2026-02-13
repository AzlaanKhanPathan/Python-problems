# Write a program to find the LCM of two numbers

def find_lcm(a,b):
    greater = max(a,b)
    smallest = min(a,b)
    for i in range(greater,a*b+1,greater):
        if i % smallest == 0:
            return i 
        
print(find_lcm(12,15))