# Print welcome message and prompt user for input
print("Welcome to the tip calculator!")
totalbill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

# Calculate the amount of money each person needs to pay
money1 = float(totalbill) / int(people)  # Divide the total bill by the number of people
money = round(money1, 2)  # Round to 2 decimal places
print(money)  # Test the calculation result

# Calculate the tip amount based on the percentage entered
tip1 = int(tip) / 100
print(tip1)  # Test the calculation result

# Calculate the total amount each person needs to pay after adding the tip
finalmoney1 = round((money * tip1) + money1, 2)
finalmoney="finalmoney1:{:.2f}".format( finalmoney1 )
print(finalmoney)  # Test the calculation result

# Print the amount each person needs to pay
print("Each person should pay: " + str(finalmoney))  # Use string concatenation
print(f"Each person should pay: ${finalmoney}")  # Use f-string to insert the value into the string



