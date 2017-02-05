# This code is for Assignment 1, MAN6915, due: Feb 5
#
# Program #1: Create a program that prompts for your name and prints a greeting using your name.
# Constraint: Keep the input, string concatenation, and output separate

def program_1():
    print("Program 1")
    #Ask for input, store in new variable, name
    name = input("What is your name? ")

    #Create output that concatenates multiple strings and the input name
    output = "Hello, {} nice to meet you!".format(name)

    #Print output
    print(output)

#Program #2: Create a program that prompts for an input string and displays output that shows the input string and
# the number of characters the string contains.
#Constraints: Be sure the output contains the orginal string. Use a single output statement to construct the output.
# Use a built-in function to determine the length of the string.

def program_2():
    print("Program 2: Number of Characters in a string") #What the upcoming input is for

    #Ask for input, store in new variable, input_string
    input_string = input("What is the input string? ")

    output = "{} has {x} characters.".format(input_string, x=len(input_string))

    #Single print and output statement that concatenates the input_string with its length in a full sentence.
    print(output)

#Program #3: Create a simple mad-lib program that prompts for a noun, a verb, an adverb, and an adjective and
# injects those into a story that you create
#Contraints: Use a single output statement for this program

def program_3():
    print("Program 3: Mad-lib") #What the upcoming input is for

    #Ask for inputs: noun, verb, adjective, adverb
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    #Create a story, using the inputs above. Use one output and print statement

    output = "The {} {} {} {} in the Summertime! Hilarious!".format(adjective, noun, adverb, verb)

    print(output)


#Program #4: Write a program that prompts for two numbers. Print the sum, difference, product,
# and quotient of those numbers
#Constraints: Values coming from users will be strings. Ensure that you convert these value to numbers before
# doing the math. Keep the inputs and outputs separate from the numerical conversions and other processing. Generate a
# single output statement with line breaks in the appropriate spots.

def program_4():
    print("Program 4: Simple Math") #What the upcoming input is for

    #Ask for inputs: number_1 and number_2. These need to be numbers, not strings. Use int() to
    # explictly state this in the input. This will generate an error if the user tries to enter something other than a
    # whole number (integer.)
    number_1 = int(input("What is the first number? (Enter an integer) "))
    number_2 = int(input("What is the second number? (Enter an integer) "))

    #Find the sum, difference, product, and quotient. Careful to use expanded variable names due to built-in functions in Python
    sum_of_numbers = number_1 + number_2
    difference_of_numbers = number_1 - number_2
    product_of_numbers =  number_1 * number_2
    quotient_of_numbers =  number_1 / number_2

    #Print results, using line breaks to print on different lines

    output = "{} + {} = {} \n" \
             "{} - {} = {} \n" \
             "{} * {} = {} \n" \
             "{} / {} = {}".format(number_1, number_2, sum_of_numbers,
                                   number_1, number_2, difference_of_numbers,
                                   number_1, number_2, product_of_numbers,
                                   number_1, number_2, quotient_of_numbers)
    print(output)


#Program #5: Create a program that determines how many years you have left until retirement and the year you can retire.
# It should prompt for your current age and the age you want to retire
# Constraints: Again, be sure to convert the input to numerical data before doing any math. Don’t hard-code the current
#  year into your program. Get it from the system time via your programming language.

def program_5():
    print("Program 5: Years Until Retirement") #What the upcoming input is for

    #First, gather your inputs, current_age and retirement_age. These need to be numbers, not strings. Use int() to
    # explictly state this in the input. This will generate an error if the user tries to enter something other than a
    # whole number (integer.)
    current_age = int(input("What is your current age? "))
    retirement_age = int(input("At what age would you like to retire? "))

    # Create variable for number of years left until retirement
    years_left = retirement_age - current_age

    #Import module to do date and time calculations using the current system time
    import datetime
    now = datetime.datetime.now() #This creates an easy way to reference the year as now.year for our calculations

    #Create variable for retirement year, using now.year that we just imported and years_left calculated earlier
    retirement_year = now.year + years_left

    output = "You have {} years left until you can retire. \n" \
             "It's {}, so you can retire in {}.".format(years_left, now.year, retirement_year)

    #Print output, concatenating strings and using line breaks.
    print(output)

#Program #6: Create a program that calculates the area of a room. Prompt the user for the length and width of the room
#  in feet. Then display the area in both square feet and square meters.
#Constraints: Keep the calculations separate from the output. Use a constant to hold the conversion factor.

def program_6():
    print("Program 6: Area of a Room") #What the upcoming input is for

    #Ask use input for length_of_room_feet and width_of_room_feet. Defining the input as a float. User can input a float or
    #  an integer with no problems, but will get an error message if trying to enter something else (i.e. string like
    #  "3 feet, 6 inches")
    length_of_room_feet = float(input("What is the length of the room in feet? "))
    width_of_room_feet = float(input("What is the width of the room in feet? "))

    #Calculate and store square_feet from user inputs
    square_feet = length_of_room_feet * width_of_room_feet

    #Calculate and convert square_feet to square_meters
    square_meters = square_feet * 0.09290304

    #Print retults, confirming user inputs, square feet results, and conversion to square meters. Use line breaks
    output = "You entered dimensions of {} feet by {} feet.\n" \
             "The area is:\n" \
             "{} square feet, which is:\n" \
             "{:.2f} square meters.".format(length_of_room_feet, width_of_room_feet, square_feet, square_meters)
    print(output)


#Program #7: Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, and the
#  number of slices per pizza. Ensure that the number of pieces comes out even. Display the number of pieces of pizza
#  each person should get. If there are leftovers, show the number of leftover pieces.

def program_7():
    print("Program 7: Pizza Party") #What the upcoming input is for

    #First, ask user for number_of_people, number_of_pizzas, and slices_per_pizza. These need to be numbers, not strings.
    # Use int() to explictly state this in the input. This will generate an error if the user tries to enter something
    # other than a whole number (integer.)
    number_of_people = int(input("How many people? "))
    number_of_pizzas = int(input("How many pizzas do you have? "))
    slices_per_pizza = int(input("How many slices per pizza? "))

    #Calculate the slices_per_person & leftover_slices using the divmod function
    slices_per_person, leftover_slices = divmod((slices_per_pizza*number_of_pizzas), number_of_people)

    #Print output, confirming inputs, how many slices each person gets, and how many leftover slices remain. Use line breaks
    output = "{} people with {} pizzas. \n" \
             "Each person gets {} slices of pizza. \n" \
             "There are {} leftover slices of pizza.".format(number_of_people, number_of_pizzas, slices_per_person, leftover_slices)
    print(output)

#Program #8: Calculate gallons of paint needed to paint the ceiling of a room. Prompt for the length and width, and
#  assume one gallon covers 350 square feet. Display the number of gallons needed to paint the ceiling as a whole number.
#Constraints: Use a constant to hold the conversion rate. Ensure that you round up to the next whole number.

def program_8():
    print("Program 8: Gallons of Paint") #What the upcoming input is for

    #Ask user for length_of_ceiling and width_of_ceiling in feet.  Defining the input as a float. User can input a float or
    #  an integer with no problems, but will get an error message if trying to enter something else (i.e. string like
    #  "3 feet, 6 inches")

    length_of_ceiling = float(input("What is the length of the ceiling, in feet? "))
    width_of_ceiling = float(input("What is the width of the ceiling, in feet? "))

    #Calculate square feet of the ceiling and store in sf_ceiling
    sf_ceiling = length_of_ceiling * width_of_ceiling

    #Calculate gallons of paint needed, assuming one gallon covers 350 sq ft.
    gallons_of_paint = sf_ceiling / 350

    #Use the ceiling (pun intended) function in the Python math module to round result up. Import math
    #Convert to int since we know this will be a whole number
    import math
    purchased_gallons = int(math.ceil(gallons_of_paint))

    #Print output, including number of gallons needed and calculated square footage. Use line break
    output = "You will need to purchase {} gallons of \n" \
             "paint to cover {} square feet.".format(purchased_gallons, sf_ceiling)
    print(output)


#Program 9: Create a simple self-checkout system. Prompt for the prices and quantities of three items. Calculate the
#  subtotal of the items. Then calculate the tax using a tax rate of 5.5%. Print out the line items with the quantity
#  and total, and then print out the subtotal, tax amount, and total.
#Constraints: Keep the input, processing, and output parts of your program separate. Collect the input, then do the math
#  operations and string building, and then print out the output. Be sure you explicitly convert input to numerical data
#  before doing any calculations

def program_9():
    print("Program 9: Self Check-Out") #What the upcoming input is for

    #Ask user for inputs, price_item_1, qty_item_1, price_item_2, qty_item_2, price_item_3, qty_item_3. Defining the input
    #  as a float. User can input a float or an integer with no problems, but will get an error message if trying to enter
    #  something else (i.e. string like "3 dollars and 50 cents")

    price_item_1 = float(input("Enter the price of item 1: $"))
    qty_item_1 = float(input("Enter the quantity of item 1: "))
    price_item_2 = float(input("Enter the price of item 2: $"))
    qty_item_2 = float(input("Enter the quantity of item 1: "))
    price_item_3 = float(input("Enter the price of item 3: $"))
    qty_item_3 = float(input("Enter the quantity of item 1: "))

    #Calculate the subtotal
    subtotal = (price_item_1 * qty_item_1) + (price_item_2 * qty_item_2) + (price_item_3 * qty_item_3)


    #Calculate tax, using the tax_rate of 5.5%. Since we're using dollars, we'll round our result to 2 decimal places
    import decimal
    tax_rate = 0.055
    tax = subtotal * tax_rate

    #Calculate total from subtotal & tax
    total = subtotal + tax

    #Print results with labels, formatting the subtotal to display two decimals if an even dollar amount
    output = "Subtotal: ${:.2f}\n" \
             "Tax: ${:.2f}\n" \
             "Total: ${:.2f}".format(subtotal, tax, total)
    print(output)


#Program 10: Create a program that computes simple interest. Prompt for the principal amount, the rate as a percentage,
#  and the time, and display the amount accrued (principal + interest).
#Constraints: Prompt for the rate as a percentage (like 15, not .15). Divide the input by 100 in your program. Ensure
# that fractions of a cent are rounded up to the next penny. Ensure that the output is formatted as money.

from decimal import * #needed for ROUND_UP calculation in Program 10

def program_10():
    print("Program 10: Simple Interest") #What the upcoming input is for

    #First, ask for user inputs for the principal, per_interest_rate, and number_of_years
    principal = float(input("Enter the principal amount:$"))
    per_interest_rate = float(input("Enter the interest rate (as a percentage): "))
    number_of_years = float(input("Enter the number of years: "))

    #Covert rate_of_interest from percentage to decimal
    dec_interest_rate = per_interest_rate/100

    #The formula for simple interest is A = P(1 + rt), where P is the principal amount, r is the annual rate of interest,
    # t is the number of years the amount is invested, and A is the amount at the end of the investment.
    # Calculate simple interest. Ensure that fractions of a cent are rounded up to the next penny (import Decimal)

    investment_worth = principal*(1 + (dec_interest_rate * number_of_years))
    rounded_investment_worth = Decimal(investment_worth).quantize(Decimal('.01'), rounding=ROUND_UP)

    #Print a statement that includes the years invested, interest rate, and investment worth.
    #  Ensure the output is formatted as money
    output = "After {:.0f} years at {}%, the investment will\n" \
             "be worth ${:.2f}.".format(number_of_years, per_interest_rate, rounded_investment_worth)
    print(output)

#Call all programs
program_1()
program_2()
program_3()
program_4()
program_5()
program_6()
program_7()
program_8()
program_9()
program_10()