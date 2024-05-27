from art import logo
class SingleString:
    def __init__(self):
        self._value = None
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Can only assign string values (str)")
        self._value = new_value
print(logo) 
i=False
finalbid=0
finalname=SingleString()
while not i==True:
 name=(input("What's your name: "))
 bid=int((input("What is your bid: ")))
 if finalbid <bid:
  finalbid=bid
  finalname.value=name
 bidder=input("Are there any other bidders? Type 'yes or 'no'.")
 if bidder.lower()=="yes":
  i=False
 else:
  print(f'The winner is {finalname.value} with a bid of {finalbid}')
  i=True



