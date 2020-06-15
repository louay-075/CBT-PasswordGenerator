from string import digits, ascii_letters
from random import choice, shuffle


########################################
#this small program generate a password you can use it to secure your accounts with a strong password!!!
# How it works!!!!
# simply choose the length of the letters and the numbers and the program will generate a random password depend of the numbers of letters and number that you chose !
# Author : Louay El-oudi || Blind programmer
# Email : louay.eloudi@gmail.com
# Youtube channel : cyberblindtech
########################################

print 'Cyberblindtech password generator'
print
print 'Author : Louay El-oudi'
print 
print 'Emil : louay.eloudi@gmail.com'
print
print 'Youtube channel : cyberblindtech'

# take the length of letters and digits numbers from user to generate a password
letter = int(raw_input('length of letters password will containe: '))

number = int(raw_input('length of digits numbers password will containe: '))

#generate a random numbers from the given input
numbers = ''.join([choice(digits) for n in range(number)])

# generate a random letters from the given input
letters = ''.join([choice(ascii_letters) for n in range(letter)])

# combine them together
password = letters+numbers

# store the password into a list
pwd = list(password)

# scramble the password
shuffle(pwd)

# store the password 
result = ''.join(pwd)

# write the password into a file
with open('CBT-PASSWORDGENERATOR.txt', 'a+') as f:
    f.write(result+'\n')

print "[*] Password of %d length generated successfully ... Saved at CBT-PASSWORDGENERATOR.txt file" % (len(password))

raw_input('Press ENTER to quit!')