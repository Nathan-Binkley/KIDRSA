import math, re
from decimal import *

print("What message would you like to encrypt?")
message = input()
message = message.lower()
message = re.sub('[\s+]', '', message)
print("Give me 4 numbers")
a = input()
b = input()
c = input()
d = input()


M = a*b-1
pub_key = int(c) * M + int(a)
priv_key = int(d) * M + int(b)
n = (pub_key * priv_key - 1) // M


message_list = []
char_list = []

for i in message:
    message_list.append(i)
    char_list.append(ord(i))

print("Your public key is: " + str(pub_key))
print("Your private key is: " + str(priv_key))
print("Your n keys are: " + str(n))
print("Your M values are: " + str(M))

encrypted_list_char = []
encrypted_list = []

for i in message_list:
    encrypted_list.append(int(ord(i) * pub_key % n))
    encrypted_list_char.append(chr(int(ord(i) * pub_key % n)))

print("Your plaintext is: " + str(message_list))
print("Your values are: " + str(char_list))
print("Your encryption is: " + str(encrypted_list))
print("Your char encryption is: " + str(encrypted_list_char))

original_list = []


for i in encrypted_list:

    original_list.append(chr(int(i * priv_key % n)))

print("Original message is: " + str(original_list))
