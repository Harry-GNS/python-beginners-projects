credit_card_number= input("Enter your credit card number: ").replace(" ", "").replace("-", "")

if credit_card_number.isdigit() and len(credit_card_number)>=4:
    last_4_numbers= credit_card_number[-4:]

    print(f"XXXX-XXXX-XXXX-{last_4_numbers}")

else:
    print("Invalid credit card number")

