import string

def shiftright(letter,shift): # shift right 
 alphabet = string.ascii_letters
 index=alphabet.index(letter)
 finalleter=alphabet[(index+shift)%26]
 return finalleter
def shiftleft(letter ,shift):   #shift left 
 alphabet = string.ascii_letters
 index=alphabet.index(letter)
 finalleter=alphabet[(index-shift)%26]
 return finalleter

final=[]
x=bool
while not x==True:
 print("Type 'encode' to encrypt, type 'decode' to decrypt:")
 a=input()
 

 if a=="encode": 
    print("Type your message: \n")
    sentence=input()
    print("type the shift number: \n")
    shift=int(input())
    for i in sentence:
        j=0
        final+=shiftright(i,shift)
    print(f"here the encode's result: {"".join(final)} \n")
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    end=input()
    if end=="yes": 
       final=[]
       end=False
    else:
        final=[]
        end=True

# a=shiftleft("a",1) // Test 
 if a=="decode":
    print("Type your message: \n")
    sentence=input()
    print("type the shift number: \n")
    shift=int(input())
    for i in sentence:
        j=0
        final+=shiftleft(i,shift)
    print(f"here the encode's result: {"".join(final)} \n")
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    end=input()
    if end=="yes": 
       final=[]
       end=False
    else:
        final=[]
        end=True
# print(a) // Test 






