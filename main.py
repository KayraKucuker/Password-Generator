import random

characters = "aMc?!=)13457/(+%^!'^+:_2156" #-- You can edit this if you want its just characteristics.

length = int(input("How many characters should your password be? "))

password = ""
for _ in range(length):
    password += random.choice(characters)

print("Your password:", password)
