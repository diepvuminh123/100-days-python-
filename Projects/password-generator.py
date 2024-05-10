#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    #print(random.randrange(3, 9))
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
sum=nr_letters+nr_symbols+nr_numbers
i=0
j=0
k=0
preps=[]
fnps=[]
while i< nr_letters:
    preps.append(random.choice(letters))
    i+=1
while j<nr_symbols:
    preps.append(random.choice(symbols))
    j+=1
while k<nr_numbers:
    preps.append(random.choice(numbers))
    k+=1
#password
print(preps)
random.shuffle(preps)
#print(preps)
print("The password is : ")
for x in preps:
    print(x,end="")










 


