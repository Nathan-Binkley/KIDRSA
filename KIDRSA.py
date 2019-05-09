## Nathan Binkley
## BSCS CPSC Clemson University
## Written May 7th 2019

import math, re
from decimal import *

print("What message would you like to encrypt?")
message = input()
message = message.lower()
message = re.sub('[\s+]', '', message)
a=None
b=None
c=None
d=None
while True:
    try: #input validation
        print("Give me 4 numbers")
        a = input()
        b = input()
        c = input()
        d = input()
        M = int(a)*int(b)-1
        pub_key = int(c) * M + int(a)
        priv_key = int(d) * M + int(b)

    except ValueError: #value error indicates wrong convert type (ie Null (None) --> int)
                        # when not possible
        print("Something went wrong, please try again")
        continue
    else:
        break





message_list = []
char_list = []

for i in message:
    message_list.append(i)
    char_list.append(ord(i))



encrypted = ""
encrypted_list = []

for i in message_list:
    encrypted_list.append(int(ord(i) * pub_key % n))

    encrypted += str(chr(int(ord(i) * pub_key % n)))

print("Your plaintext is: " + message)
print("Your values are: " + str(char_list))
print("Your encryption is: " + str(encrypted_list))
print("Encrypted: " + encrypted)


original_list = []
original = ""

for i in encrypted_list:
    original_list.append(chr(int(i * priv_key % n)))
    original += chr(int(i * priv_key % n))

print("Original message is: " + original)
