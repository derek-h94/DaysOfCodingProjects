#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")

#Prompt user to enter values for bill, tip, and people amounts variables
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))

#function to calculate tip amount
tip_amount = tip / 100
tip_amount += 1

#function to calculate amount owed for each person
total_amount_owed = (bill / people) * tip_amount

# #functions to format calcualation to include two decimal numbers
final_amount = round(total_amount_owed,2)
final_amount = "{:.2f}".format(total_amount_owed)

#prints the final amount that each person will owe
print(f"Each person owes: ${final_amount}")
