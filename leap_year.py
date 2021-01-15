# Code by Natalie Borgorez

# Find out whether it's a leap year by telling it to my Python program!

year = int(input("Enter a year:  "))

if year % 4 == 0 and year % 100 != 0:
        print("%i is a leap year" % year)

elif year % 100 == 0 and year % 400 == 0:
        print("%i is a leap year" % year)

else:
        print("%i is not a leap year" % year)

# Code by Natalie Borgorez















