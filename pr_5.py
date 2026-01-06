# Write a python program to print largest number 

def largest_num(a,b,c):
    if a > b and a > c :
        print(a)
    elif b > a and b > c :
        print(b)
    else: 
        print(c)

largest_num(50,150,20)