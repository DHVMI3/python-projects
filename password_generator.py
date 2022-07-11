# Password Generator

import random

lowcase = "qwertyuiopasdfghjklzxcvbnm"
uppercase = lowcase.upper()
numb = "1234567890"
symb = '!@#$%&^*()_-+={}[]:;<,>.?'

char = lowcase + uppercase + numb + symb

print("".join(random.sample(char, 8)) )