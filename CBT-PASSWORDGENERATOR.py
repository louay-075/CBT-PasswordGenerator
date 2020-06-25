from string import digits, ascii_letters, punctuation 
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
print 'Email : louay.eloudi@gmail.com'
print
print 'Youtube channel : cyberblindtech'

# take the length of symbol, letters and digits numbers from user to generate a password
letter = int(raw_input('How many letter you want in your password: '))

number = int(raw_input('How many number you want in your password: '))

symbol = int(raw_input('How many symbol you want in your password: '))

#generate a random numbers from the given input
numbers = ''.join([choice(digits) for n in range(number)])

# generate a random letters from the given input
letters = ''.join([choice(ascii_letters) for n in range(letter)])

# generate a random symbols from the given input
symbols = ''.join([choice(punctuation ) for n in range(symbol)])

# combine them together
password = letters+numbers+symbols

# store the password into a list
pwd = list(password)

# scramble the password
shuffle(pwd)

# store the password 
result = ''.join(pwd)

# print out the generated password
print 'Your password is : ', result
# save the password into a file
with open('pass.txt', 'a+') as f:
    f.write('\n'+result+'\n')

print "[*] Password of %d length generated successfully ... Saved at pass.txt file" % (len(password))

raw_input('Press ENTER to quit!')
