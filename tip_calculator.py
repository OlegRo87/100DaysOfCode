print("Welcome to the tip calculator!")
bill_input = input("What was the total bill? ")
tip_input = input("How much tip would you like to give? 10, 12, or 15? ")
tip = int(tip_input) / 100 + 1
amount_of_people = input("How many people to split the bill? ")
tip_amount = round(float(bill_input) * float(tip) / int(amount_of_people), 2)

print(f"Each person should pay: {tip_amount}")