import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
mylist=[rock, paper, scissors]
choice=int(input())
print("the user:")
if choice==0:
 print(mylist[0])
elif(choice==1):
 print(mylist[1])
elif(choice==2):
 print(mylist[2])
else: 
 print("You fail")
computer=random.choice(mylist)
print("The computer: \n")
if computer==rock:
 print(mylist[0])
elif computer==paper:
 print(mylist[1])
elif computer==scissors: 
 print(mylist[2])
print("The result is: ")
#user choices rock
if choice==0:
 if computer==rock:
  print("Draw")
 elif computer==paper:
  print("You lose")
 else:
  print("You win")
#user choices paper
if choice==1:
 if computer==rock:
  print("You win")
 elif computer==paper:
  print("Draw")
 else:
  print("You Lose")
#user choices scissor
if choice==2:
 if computer==rock:
  print("You lose")
 elif computer==paper:
  print("You win")
 else:
  print("Draw")

 
 

