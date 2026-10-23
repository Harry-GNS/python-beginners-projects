import random
import string


options1 = list(string.printable)   
options2 = options1.copy()          
random.shuffle(options2)            


message = input("Enter the message: ")

encrypted_msg = ""
for letter in message:
    index = options1.index(letter)   
    encrypted_msg += options2[index] 

print(f"Original message:{message}")
print(f"Encrypted message:{encrypted_msg}")

decrypted_msg=""
for quantity in encrypted_msg:
    location=options2.index(quantity)
    decrypted_msg+=options1[location]

ask=input("Press Y to decrypt the message: ").upper()
if ask=="Y":
    print(f"Decrypted message: {decrypted_msg}")  
else:
    print("Invalid option") 
