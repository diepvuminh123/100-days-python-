import string

def shiftright(letter,shift):
 alphabet = string.ascii_letters
 index=alphabet.index(letter)
 finalleter=alphabet[(index+shift)%26]


 return finalleter
        
# print("Type 'encode' to encrypt, type 'decode' to decrypt:")
# a=input()
# if a=="encode": 
#     print("Type the sentence: \n")
#     sentence=input()
#     print("type the shift: \n")
#     shift=int(input())
a=shiftright("z",1)
print(a)






