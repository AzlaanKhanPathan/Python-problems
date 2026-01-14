# Create a program to count the number of vowels in a string.
# self made logic 
def checking_vowels(str):
    for char in str:
        if char in 'aeiou':
            return char 


print(checking_vowels("Optimus Prime"))

# CodeWars Version 
def get_count(sentence):
    vowels = ('a','e','i','o','u')
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1 
    return count 
            
print(get_count("aeiou"))