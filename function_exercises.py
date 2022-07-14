# Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.

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
    '''calculate_tip:
    parameters: b, t  two numerical values, t requiring a percent.
    Will mutiply the Bill price (b) by the percentage you want to tip (t) to find the amount of money needed for tip.
    '''

    if t <= 0 or t >= 1:
        return "Please enter a valid tip percentage [ex: .20, 0.20]"
    else:
        tip = b * t
        return "You should tip ${:.2f}".format(tip)
        # this formats the number to return the number to the tenths place.


# Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.





# Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.





# Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).





# Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.





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





# Write a function named cumulative_sum that accepts a list of numbers and returns a list 
# that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]





# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.





# Create a function named col_index. It should accept a spreadsheet column name, and 
# return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27





# 