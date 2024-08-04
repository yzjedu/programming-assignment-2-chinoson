# Step 0: Intro comment here
# Programmer: Henderson Fryer
# Course: CS701/GB-731, Dr. Yalew
# Date: 8/3/2024
# Programming Assignment: 2
# Program Inputs: Month (as a number in the range 1 through 12), Year
# Program Outputs: Number of days in the given month

def main():

    # Step 1: Ask the user for the month and year

    month = int(input("Enter month as a number (1-12):"))
    if month <= 0 or month > 12:
        print("Invalid month")
    else:
        year = int(input("Enter year (ex. 1999):"))

    # Step 2: Determine if the year is a leap year
    

        if year % 100 == 0 and year % 400 == 0:
                isLeapYear = True
        elif year % 4 == 0:
                isLeapYear = True
        else:
            isLeapYear = False


    # Step 3: Determine the number of days in the month

        thirtyDays = [4, 6, 9, 11]
        thirtyOneDays = [1, 3, 5, 7, 8, 10, 12]

        if isLeapYear and month == 2:
            monthDays = 29
        elif month in thirtyDays:
            monthDays = 30
        elif month in thirtyOneDays:
            monthDays = 31
        else:
            monthDays = 28
    

    # Step 4: Output the number of days in the month

        print('The month has', monthDays, 'days.')
   
   #pass

if __name__ == "__main__":
    main()