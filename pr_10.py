# Check if a number is a palindrome

def palindrome_check(n):
    s = str(abs(n))
    length = len(s)

    for i in range(length // 2): # loop through half of string 
        if s[i] != s[length - i - 1]: #check the first and last index of string 
            return False
    
    return s, True 


print(palindrome_check(1232))