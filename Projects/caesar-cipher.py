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
print("Type 'encode' to encrypt, type 'decode' to decrypt:")
a="encode"
if a=="encode": 
    print("Type the sentence: \n")
    sentence="abc"
    print("type the shift: \n")
    shift=2
    for i in sentence:
      j=0
      final+=shiftright(i,shift)
# a=shiftleft("a",1) // Test 

print("".join(final))
# print(a) // Test 






