def odd_even():
    """Check if a number is odd or even."""

    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

odd_even()