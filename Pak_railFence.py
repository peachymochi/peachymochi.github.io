"""
Asks user whether they want to encrypt or decrypt their message.
Written By: Grace Pak
"""
x = input("Would you like to 'encrypt' or 'decrypt' your message?: ")

if x == "Encrypt" or x == "encrypt":
    a = input("Please enter in your message: ")
    
elif x == "Decrypt" or x == "decrypt":
    a = input("Please enter in your message: ")
    
"""
This program takes a sentence/message and scrambles the text.
It stores the even indexed characters into an accumulator string and
the odd indexed characters into another accumulator string.
It will then separate them into two separate string and then concatenate them
into one to create an encrypted message.
----------------------------------------------------------------------------
Written By: Grace Pak
Sources: https://www.youtube.com/watch?time_continue=559&v=qOlJwi9mu2Q
         Rail Fence Cipher - profecali
"""      
def Scramble2Text(plainText): 
   evenChars = ""
   oddChars = ""
   charCount = 0

   for ch in plainText:
      if charCount % 2 is 0:
         evenChars = evenChars + ch
      else:
         oddChars = oddChars + ch

      charCount = charCount + 1

   cipherText = oddChars + evenChars

   
   
   return cipherText

msg = Scramble2Text(a)

print(msg)

"""
This program basically does what the previous program does, however,
this program takes the encrypted message and changes it into a decrypted
message.
---------------------------------------------------------------------------
Written By: Grace Pak
Sources: https://www.youtube.com/watch?v=uaCumJi4Iuw
         Rail Fence Cipher: Part 2 - profecali
"""
def decryptMessage(cipherText):
    halfLength = len(cipherText)//2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]


    plainText = ""
    
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars) > len(oddChars):
        plainText = plainText + evenChars[-1]


    return plainText

plain = decryptMessage(a)

print(plain)


