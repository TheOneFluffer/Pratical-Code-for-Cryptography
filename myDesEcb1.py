#!/usr/bink/env python3
#ST2504 - ACG Practical - myDES_ECB
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad  #  load the crypto libraries
## Extra function to be called by main program
## if num = 8,16,32 return true, false otherwise
def chk_eight(num):
    num1 = num % 8
    if not num1 : return True
    return False
    
# start main function
BLOCK_SIZE = 8  # Size of DES cipher data block size 64 bit
original_text='Hello123Hello123Hello123'
text_in_bytes = original_text.encode()  # convert UTF 8 encoded string to bytes
# Google or ask around for diffferences between 
#     bytes, UTF-8 encoding, Unicode encoding
print("Generating a 56-bit DES key ...")
key=get_random_bytes(8) # generate randmom bytes for DES key 64 bit
# key size for DES 8 bytes (64 bits), only use 56 bits
print("The key is generated.\n")
print("Plaintext:")
for x in range(1, 4):
    for b in text_in_bytes:  # text_in_bytes is a byte array    
        print(format(b, '02X'),end=" ")
    print("\n")
    # Note the indent is needed as part of the looping
    # [end=] specify what is added @ the end of line
    # format will format the byte to various format with a given template
    # see https://www.programiz.com/python-programming/methods/string/format
print("\n") # print a newline
cipher = DES.new(key, DES.MODE_ECB)  # new DES cipher using key generated
cipher_text_bytes = cipher.encrypt(pad(text_in_bytes,BLOCK_SIZE)) # encrypt data
# data is bytes (text_in_bytes), not strings
print("Ciphertext (in base 10 - Decimal):")
for x in range(1, 4):
    for b in cipher_text_bytes: 
        print(format(b, '03d'),end=" ")  # formatting - 3 places, Dec
    print("\n")
print("\n")
print("Ciphertext (in base 16 - Hex):")
for x in range(1, 4):
    for b in cipher_text_bytes:
        print(format(b , '02X'),end=" ")  # formatting - 2 places, Hex
    print("\n")
print("\n")

# ** Decrypt message here *********

# create a new DES cipher obj ect with the same key and mode  
my_cipher = DES.new(key, DES.MODE_ECB) 

# Now decrypt the text using your new cipher
plain_text_bytes = unpad(my_cipher.decrypt(cipher_text_bytes), BLOCK_SIZE )

# Print the message in UTF8 (normal readable way
print ("Decrypted text: ", plain_text_bytes.decode() )
