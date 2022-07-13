# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

def movierental(days):
    price_of_movie_perday = 3
    rentalfee = price_of_movie_perday * days
    print("$ " + str(rentalfee) + " for " + str(days) + " day(s)")
    return rentalfee

lm = movierental(3) #(giving 9)
bb = movierental(5) #(giving 15)
herc = movierental(1) # (giving 3)
total = lm + bb + herc
print("$" + str(total) + " to rent the movies.")

assert movierental(3) == 9
assert movierental(5) == 15
assert movierental(1) == 3




# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_PayPH = 400
amazon_PayPH = 380
fB_PayPH = 350
google_Hours = 6
amazon_Hours = 4
fB_Hours = 10

salary_This_Week = (google_PayPH * google_Hours) * (amazon_PayPH * amazon_Hours) * (fB_PayPH * fB_Hours)
print("$" + str(salary_This_Week) + " made this week.")




# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.


def can_Enroll(room,time):
    if room == True and time == True:
        print("Can Attend")
        return "yes"
    elif room == True and time == False:
        print("No, Scheduling Conflict.")
        return "sch"
    elif room == False and time == True:
        print("No, The class if full.")
        return "time"
    else:
        print("No, The class is full, and there's a Scheduling conflict.")
        return "both"

assert can_Enroll(True,True) == "yes"
assert can_Enroll(True,False) == "sch"
assert can_Enroll(False,True) == "time"
assert can_Enroll(False,False) == "both"


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.


def offervalid(items,date,prem):
    itemcheck = (items > 2)
    datecheck = (date < 8012022)
    if itemcheck == True and datecheck == True or prem == True and datecheck == True:
        print("Congratulations! This offer is Valid!")
        return True
    elif itemcheck == False or datecheck == False:
        print("Sorry, this is not a Valid offer, please check number of items or current date!")
        return False

assert offervalid(2,7122022,False) == False
assert offervalid(2,7122022,True) == True
assert offervalid(4,7122022,False) == True
assert offervalid(2,9122022,True) == False
assert offervalid(6,9122022,False) == False
    



# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

def username_and_password(name,password):
    strusername = str(name)
    strpassword = str(password)
    a = (len(strpassword) >= 5)
    b = (len(strusername) <= 20)
    c = (strpassword != strusername)
    d = strusername.strip() == strusername
    e = strpassword.strip() == strpassword
    if a == False or b == False or c == False or d == False or e == False:
        print("Please try another username or password")
        return False
    else:
        print("Your Username and Password have been accepted")
        return True



assert username_and_password("codeup","notastrongpassword") == True