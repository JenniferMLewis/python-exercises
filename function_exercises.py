# Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.

from curses.ascii import isdigit
from lib2to3.pytree import LeafPattern


def is_two(x):
    '''
    is_two:
    parameters: x, an int or string variable
    return True or False, dependant upon whether x is numerical 2, string "2" or "two" or another not two input.
    '''
    if x == 2 or x == "2" or x == "two":
        return True
    else:
        return False
    # EASIER: 
        # def is_two(x): 
            # return x == 2 or x == "2" or x == "two"


# Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.

def is_vowel(a):
    '''
    is_vowel:
    parameters: a, a string variable (single letter please)
    returns True or False dependant upon whether the entered letter is a vowel or not. For this 'Y' is not a vowel.
    '''
    vowels = ["a", "e", "i", "o", "u"]
    if a.lower() in vowels:
        return True
    else:
        return False
        # if type(a) == str: 
            # if len(a) == 1: 
                # return a.lower() in list('aeiou') 
            # else: return False 
        # else: return False


#Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(b):
    '''
    is_consonant:
    parameters: b, a string variable (single letter please)
    returns True or False dependant upon whether the entered letter is a consonant or not. For this "Y" is a consonant.
    this function calls upon the "is_vowel" function and returns the opposite result.
    '''
    if is_vowel(b) == True:
        return False
    else:
        return True

# Define a function that accepts a string that is a word. The function should capitalize the first 
# letter of the word if the word starts with a consonant.

def con_caps(s):
    '''
    con_caps:
    parameters: s, a string variable
    Checks if the first letter of a string, and capitalises it if the letter is a consonant.
    Utilises the "is_vowel" and "is_consonant" functions.
    '''
    fl = s[0]
    if is_consonant(fl) == True:
        s = fl.upper() + s[1:]
        return s
    else:
        return s

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.


def calculate_tip(b, t):
    '''
    calculate_tip:
    parameters: b, t  two numerical values, t requiring a percent.
    Will mutiply the Bill price (b) by the percentage you want to tip (t) to find the amount of money needed for tip.
    '''
    if t > 0 or t < 1:
        tip = b * t
        return "You should tip ${:.2f}".format(tip)
        # this formats the number to return the number to the tenths place.
    else:
        return "Please enter a valid tip percentage [ex: .20, 0.20]"


# Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.


def apply_discount(o, d):
    '''
    apply_discount:
    parameters: o, d   two numerical values, d requiring a percent.
    Will multiply the original price by the discount, then remove the discount from the original price to give your new price with discount applied.
    '''
    if d > 0 or d < 1:
        dis = o * d
        new_price = o - dis
        return f"Your new price is {new_price}"
    else:
        return "Please Enter a Valid Discount Percentage [ex: .20, 0.20]"



# Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.


def handle_commas(dig):
    '''
    handle_commas:
    parameters: dig a string number with commas.
    Will remove commas from a string number returning an int number
    '''
    dig = dig.replace(",", "")
    # str.replace(old_str, new_str, [optional max times to replace])
    int(dig)
    return dig


# Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).


def get_letter_grade(g):
    '''
    get_letter_grade:
    parameters: g, an interger representing your grade percent.
    takes the numerical value and returns the letter equivelant.
    '''
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
    return f"Your grade is... {letter_grade}"


# Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.


def remove_vowels(v):
    '''
    remove_vowels:
    parameters: v, a string with or without vowels.
    Vowels are identified and removed from the string and the string is returned sans vowels.
    '''
    newv = v
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in v.lower():
        if x in vowels:
            newv = newv.replace(x,"")
    return newv

    # def remove_vowels(vowel_word):
    # new_word =
    # Not sure I can do this today.... Too slow typing. 


# Define a function named normalize_name. It should accept a string and return a valid python 
# identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
# for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed


def normalize_name(name):
    '''
    normalize_name:
    parameters: name, a string input.
    Removes any excess white space on either end, removes anything that isn't an identifier or space, turns all interior spaces into an underscore (_)
    '''
    newname = ""
    for n in name:
        if n.isidentifier() or n == ' ':
            newname += n

    return newname.strip().lower().replace(" ", "_")
# *** Chaining functions greeting.capitalize().replace("e", "a")
#    newname = name.strip()
#    for n in name:
#        if is_vowel(n) == False and is_consonant(n) == False and n != "_" and n != " ":
#            newname = newname.replace(n,"")
#        else:
#            newname = newname.replace(" ", "_")
#    return newname

# *** HOW TO JOIN A LIST FOR PICKING OUT LETTERS ***
# def remove_vowels(vowel_word)
#    new_string = []
#    [new_string.append(letter) for letter in vowel_word if not is_vowel(letter)]
#    return ''.join(new_string)



# Write a function named cumulative_sum that accepts a list of numbers and returns a list 
# that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumulative_sum(list):
    return [sum(list[:n]) for n in list]


# OR...

def cumulative_sum(list):
    newlist = []
    for n in list:
        cumusum = sum(list[:n])
        newlist.append(cumusum)
    return newlist
# [sum(mylist[:n]) for n in mylist]

# Additional Exercise

# Once you've completed the above exercises, follow the directions from 
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.





# BONUS !!

# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.





# Create a function named col_index. It should accept a spreadsheet column name, and 
# return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27





# 