import random
import string


# string.printable also holds tab and newline characters, which would break up the encrypted line
options1 = list(string.ascii_letters + string.digits + string.punctuation + " ")
options2 = options1.copy()          
random.shuffle(options2)            


message = input("Enter the message: ")

encrypted_msg = ""
for letter in message:
    if letter in options1:
        index = options1.index(letter)
        encrypted_msg += options2[index]
    else:
        encrypted_msg += letter

print(f"Original message:{message}")
print(f"Encrypted message:{encrypted_msg}")

decrypted_msg=""
for quantity in encrypted_msg:
    if quantity in options2:
        location=options2.index(quantity)
        decrypted_msg+=options1[location]
    else:
        decrypted_msg+=quantity

ask=input("Press Y to decrypt the message: ").upper()
if ask=="Y":
    print(f"Decrypted message: {decrypted_msg}")  
else:
    print("Invalid option") 
