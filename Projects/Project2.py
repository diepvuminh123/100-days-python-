print("Welcome to the tip calculator!")
totalbill= input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, or 15?")
people=input("How many people to split the bill?")
#money each person should pay 
money1=float(totalbill)/ int(people) 
money= round(money1 , 2)
print(money) #Test
#tip round 2 decimal
tip1=int(tip) / 100 
print(tip1) #Test 
#finalmoney people should pay 
finalmoney=round((money * tip1)+money1,2)
print(finalmoney) #Test 
print("Each person should pay:" + str(finalmoney)) 


