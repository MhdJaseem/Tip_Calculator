#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("how much would you link to give? 10, 12, or 15? ")
split_bill = input("How many people to split then bill? ")

bill_as_float = float(bill)
tip_as_float = float(tip)
split_as_float = int(split_bill)

tip_percentage = tip_as_float / 100 * bill_as_float
final_bill = ((tip_percentage + bill_as_float) / split_as_float)
round_result = round(final_bill, 2)

print(f"Each person should pay: ${round_result:.2f} ")
