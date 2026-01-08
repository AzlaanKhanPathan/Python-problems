# Write a python program to convert Celsius to Farhenheit 

def temperature_converter(C):
    Farhenheit = C * 9/5 + 32 
    return f"Celsius {C} \n Farhenheit: {Farhenheit}"


print(temperature_converter(50))