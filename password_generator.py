# Password Generator

import random

lowcase = "qwertyuiopasdfghjklzxcvbnm"
uppercase = lowcase.upper()
numb = "1234567890"
symb = '!@#$%&^*()_-+={}[]:;<,>.?'

char = lowcase + uppercase + numb + symb

num = int(input('Enter the number of characters: '))

print("".join(random.sample(char, num)) )
