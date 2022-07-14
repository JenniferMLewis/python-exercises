# Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
from multiprocessing.connection import answer_challenge
from urllib.request import HTTPErrorProcessor


x = input("What day of the Week is it?")
if x.lower() == "monday":
    print("Today is Monday...")
else:
    print("Today is not a Monday!")

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
x = input("What day of the Week is it?")
if x.lower() == "saturday" or x.lower() == "sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.. Good luck!")

# c. create variables and make up values for:
#   the number of hours worked in one week
#   the hourly rate
#   how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

time = input("How many hours did you work this week?")
payph = 18
if time.isnumeric() == True:
    hours = int(time)
    if hours < 40 and hours > 0:
        print(f"Your pay this week is: ${hours * payph}")
    elif hours > 40:
        ot = hours - 40
        ot_pay = payph * 1.5
        total_ot = ot_pay * ot
        print(f"You worked Overtime! Your pay is {hours * payph + total_ot}")
else:
    print("Please enter a valid numeric value.")


# Loop Basics

# While

#   Create an integer variable i with a value of 5.
i = 5
#   Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
#   Each loop iteration, output the current value of i, then increment i by one.
    i +=1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
x = 0
while x < 100:
    print(x)
    x +=2
print(x)
# Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x > -10:
    print(x)
    x -=5
print(x)
    
# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
x = 2
while x < 1000000:
    print(x)
    x *= x

# Write a loop that uses print to create the output shown below.

x = 100
while x > 0:
    print (x)
    x -=5


# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
multable = [1,2,3,4,5,6,7,8,9,10]
x = input("Please enter the number you'd like to multiply")
if x.isnumeric() == True:
    real_x = int(x)
    for m in multable:
        answer = m * real_x
        print(f" {x} * {m} is: {answer}")
else:
    print("Please enter a valid numerical value [ex: -100, 10, 42]")


# Create a for loop that uses print to create the output shown below.

duptable = [1,2,3,4,5,6,7,8,9]
x = input("Please enter the number you'd like to duplicate:")
for d in multable:
    answer = d * x
    fake_x = int(x)
    x = str(fake_x + 1)
    print(answer)


# ***EASIER WAY FOR THESE for x in range(user_numb, to_number, by_number)***
# **Will fix this up later**

# Break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if 
# they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue 
# statement to output all the odd numbers between 1 and 50, except for the number the user entered.


#  ** I DON'T NEED ALL THESE elifs BUT, THEY'RE FUN TO WRITE**
odd = input("Please enter an odd number from 1-50: ")
if odd.isnumeric() == True:
    o = int(odd)
# 50 isn't odd though... why not 49?
    for num in range(50):
        if o >=51 or o <=0:
            print("That number isn't BETWEEN 1 and 50.")
            break
        elif o % 2 == 0:
            print("You entered an EVEN number, please enter an ODD one.") 
            break
        elif num % 2 == 0:
            continue
        elif num == o:
            print(f"Whoops! Skipping ... {o}!!")
        else:
            print(f'Here is an odd number: {num}')
else:
    print("Is not a valid Numeral.")


# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive 
# number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

even = input("Please enter an even positive number to count to: ")
if even.isnumeric() == True:
    e = int(even)
    z = 0
    for num in range(e+1):
        if e > 9000:
            print("It's over 9,000! Are you trying to break your computer?")
            break
        elif e % 2 == 1:
            print("You entered an ODD number, did you even read the instructions?") 
            break
        elif num == e:
            print(num)
            print(f"The end!")
        else:
            print(z + num)
else:
    print("Is not a valid Numeral.")

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the 
# user entered down to 1.

pos = input("Please enter positive number to count down from: ")
if pos.isnumeric() == True:
    p = int(pos)
    if p > 9000:
        print("You're still trying to break your computer, aren't you?")
    else:
        while p > 0:
            print(p)
            p -=1
else:
    print("Is not a valid Numeral.")


# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz!!")
    elif n % 3 == 0:
        print("Fizz!")
    elif n % 5 == 0:
        print("Buzz!")
    else:
        print(n)

# ** There is another way with 
# if --> print FizzBuzz    continue
# if --> print Fizz     continue 
# if --> print Buzz     continue
# print(x)


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output

from tabulate import tabulate

yN = "Y"
while yN == "Y":
    num = input("What number would you like to go up to?")
    if num.isnumeric() == True:
        print(format('''Here is your table!
        '''))
        n = int(num)
        tab = []
        for x in range (1, n+1):
            answer = [x, x ** 2, x ** 3]
            tab.append(answer)
        print(tabulate(tab, headers = ["Number", "Squared", "Cubed"]))
        yn = input("Do you wish to continue? (Y/N)")
        yN = yn.upper()
    else:
        print("Please enter a valid positive integer.")



# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

cont = "Y"
while cont == "Y":
    grade = input("Please input the numerical value of your grade (0-100):")
    if grade.isnumeric() == True:
        g = int(grade)
        if g >= 99:
            letter_grade = "an A+!"
        elif g >= 88:
            letter_grade = "an A!"
        elif g >= 87:
            letter_grade = "a B+!"
        elif g >=80:
            letter_grade = "a B!"
        elif g >= 79:
            letter_grade = "a C+"
        elif g >= 67:
            letter_grade = "a C"
        elif g >= 66:
            letter_grade = "..a D+"
        elif g >= 60:
            letter_grade = "..a D"
        elif g >= 59:
            letter_grade = "...an F.. +? Can these even be a plus??"
        elif g < 59:
            letter_grade = "...an F? Uh oh."
        else:
            print("Something went wrong??")
        print(f"Your grade is... {letter_grade}")
        cont_ans = input("Do you wish to continue? (Y/N)")
        cont = cont_ans.upper()
    else:
        print("Please enter a valid numerical value")


# Another way to break out.
# At the end after  loop's last if statement, new if statement:
# user_yn = input('Do you wish to continue? (y/n))
# if user_yn.lower() != 'y"
# break
# for anything except 'y' the program will stop.

# Create a list of dictionaries where each dictionary represents a book that you have read. Each 
# dictionary in the list should have the keys title, author, and genre. Loop through the list 
# and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of
# all the books in that genre.
books = [
    {
        "title": "Alice in Zombieland",
        "author": "Icant Remember",
        "genre": "Horror",
    },
    {
        "title": "Mrs. Murphy's Mysteries",
        "author": "Sneaky Pie Brown [Cat]",
        "genre": "Mystery",
    },
    {
        "title": "More titles here to test",
        "author": "Every CoderEver",
        "genre": "Horror",
    },
    {
        "title": "Monty",
        "author": "Python",
        "genre": "Adventure",
    },
    {
        "title": "Air Speed of Swallows",
        "author": "Laiden, European",
        "genre": "Reference",
    },
    {
        "title": "She turned me into a Newt!",
        "author": "Scare D. Peasant",
        "genre": "Horror",
    },
]

gen = input("Please Enter a Genre you'd like to read:")
g = gen.lower()
if book['genre'] == g:
            print(f" Book Title: {x['title']}")
else:
    print("The only available Genres are : Horror, Mystery, Adventure, and Reference.")


# Original, over complicated... this is so much lovely.
#    
# if g == "horror":
#    for x in books:
#        if x['genre'] == "Horror":
#            print(f" Book Title: {x['title']}")
# elif g == "reference":
#     for x in books:
#        if x['genre'] == "Refrence":
#            print(f" Book Title: {x['title']}")
# elif g == "adventure":
#    for x in books:
#        if x['genre'] == "Adventure":
#            print(f" Book Title: {x['title']}")
# elif g == "mystery":
#    for x in books:
#        if x['genre'] == "Mystery":