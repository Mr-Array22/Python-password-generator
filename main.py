import string
import random

l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

char_numbers = input('Enter the length of password:')

while True:
    try:
        char_numbers = int(char_numbers)
        if char_numbers < 6:
            print('Too short length!')
            char_numbers = input('Please enter the length of password:')
        else:
            break
    except:
        print('Please enter number only')
        char_numbers = input('Please enter the length of password:')

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

part1 = round(char_numbers * (30 / 100))
part2 = round(char_numbers * (20 / 100))

password = []

for i in range(part1):
    password.append(l1[i])
    password.append(l2[i])

for i in range(part2):
    password.append(l3[i])
    password.append(l4[i])

random.shuffle(password)

password = "".join(password[0:])
print(password)
