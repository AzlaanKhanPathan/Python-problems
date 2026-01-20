# Create a number guessing game. 

# first we make a array of numbers , then make a program to run loop through every number then checking if the number is matching with the user's numbers then print

arr_1 = [10,45,55,35,47,87,3,5,96,101]

def number_guessing():
    print("----------------------------------Welcome to number guessing ------------------------------")
    user_num = int(input("Enter your number: "))

    match user_num:
        case 10:
            return f"The guessed number is {10}"
    match user_num:
        case 45:
            return f"The guessed number is {45}"
    match user_num:
        case 55:
            return f"The guessed number is {55}" 
    match user_num:
        case 35:
            return f"The guessed number is {35}"
    match user_num:
        case 47:
            return f"The guessed number is {47}" 
    match user_num:
        case 87:
            return f"The guessed number is {8747}"

print(number_guessing())