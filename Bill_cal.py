print("#######################################################################")
print("Welcome to my humble bill calculator!")

# take amount multiply it by percentage divide it by number of people to share
total_bill = float(input("please enter the total bill here $ "))
percentage_bill = int(input("what would you like to be your percentage 12 13 or 15? "))
num_of_people = int(input("please enter the number of people to share the bill ? "))

# cal = total_bill * (percentage / 100)
# result = cal + num_of_people
bill_per = percentage_bill / 100
bill = total_bill * bill_per
bills_to_share = bill + total_bill
final_bill = bills_to_share / num_of_people
rounder = round(final_bill, 2)
rounder2 = "{:.2f}".format(final_bill)
print(rounder2)

print("#######################################################################")

##################################################################################
# print("name is hard")
import datetime


class game:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name} ({self.number})"

g1 = game("GTA", 2012)
g2 = game("murtal conbert", 672)
print(g1)
print(g2)


class greet:
    def __init__(self, name: str, status):
        self.name = name
        self.status = status

    def isgreet(self):
        return (f"good day {self.name}, {self.status}")


greetings = greet("abdul", "dark")
print(greetings.isgreet())


class jokes:
    def __init__(jokers, name, location, age):
        jokers.name = name
        jokers.location = location
        jokers.age = age

    def jokerRanks(self):
        return (
            f"we greet our hero {self.name} {self.location}"
            f" {self.age}"

        )
        # return self.name, self.location

j1 = jokes("friday", "adamawa", 40)
# del j1.age
print(j1.jokerRanks())

############################################################################
# print(datetime.time())
# 365 day a year
# 52 weeks a year
# 12 month a year

# age = int(input("what is your age ? "))
# years_remaining = 90 - age
# days_remaining = 365 * years_remaining
# weeks_remaining = days_remaining * 52
# month_remaining = weeks_remaining * 12
#
# print(years_remaining)
# print(days_remaining)
#
# result = f"you have {days_remaining} days {weeks_remaining} weeks {month_remaining} months left"
# print(result)