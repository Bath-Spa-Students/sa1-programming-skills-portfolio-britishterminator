# exercise 05

# list of months and days in them.
month_days = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
    }
# User input for month 
month = int(input("Enter the month 1 to 12: "))

# check if input is valid then print answer
if month in month_days: 
    print(f"The number of days in month {month} is {month_days[month]}.")

# if user input is invalid digit then this message will print 
else: 
    print("Wrong month number! Please enter a number between 1 and 12.")



#Advanced Requirment 

# list of month numbers and days in them 

month_days = {
    1: 31,  # January
    2: 28,  # February (default for non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# asking user to enter month number
month = int(input("Please enter month from 1 to 12: "))


# check is month number is valid 
if month in month_days:

    # if month is Feb then ask if its a leap year or not 
    if month == 2:
       leap_year = input("is it a leap year? (YES/NO): ")

       # if its leap yes then  
       if leap_year == "yes":
          
          month_days[2] = 29

    # print the month number and number of days 
    print(f"the number of days in month {month} is {month_days[month]}. ")

    # print respond if wrong number is enter number greater then 12 
else: 
    print("Wrong month number! PLease enter a valid number between 1 and 12. ")