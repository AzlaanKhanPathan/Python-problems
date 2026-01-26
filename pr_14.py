#  Check if a given year is a leap year or not.

year = 2013

if year % 400 == 0:
    print(f"Leap Year: {year}")
elif year % 4 == 0:
    print(f"Leap Year: {year}")
elif year % 100 == 0:
    print(f"It is not ")
else:
    print("It is not a leap year")