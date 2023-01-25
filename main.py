# Password Generator Project
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
finalLetters = ""
finalSymbols = ""
finalNumbers = ""
finalPassword = ""

for x in range(1, nr_letters + 1):
    randomLetters = random.randint(0, len(letters) - 1)
    finalLetters = finalLetters + letters[randomLetters]

for y in range(1, nr_symbols + 1):
    randomSymbols = random.randint(0, len(symbols) - 1)
    finalSymbols = finalSymbols + symbols[randomSymbols]

for z in range(1, nr_numbers + 1):
    randomNumbers = random.randint(0, len(numbers) - 1)
    finalNumbers = finalNumbers + numbers[randomNumbers]

finalOutput = finalLetters + finalSymbols + finalNumbers




# for an in finalOutput:
#     randomPassword = random.randint(0, len(finalOutput) - 1)
#     finalPassword = finalPassword + finalOutput[randomPassword]

finalOutput = list(finalOutput)
random.shuffle(finalOutput)
finalOutput = ''.join(finalOutput)
print(f"Your password is: {finalOutput}")



# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
